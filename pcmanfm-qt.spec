%define major 2
%define libname %mklibname fm-qt5 %{major}
%define devname %mklibname fm-qt5 -d
%define git 0

Summary:	File manager for the LXQt desktop
Name:		pcmanfm-qt
Version:	0.10.0
%if %git
Release:	1.%git.1
Source0:	%{name}-%{git}.tar.xz
%else
Release:	10
Source0:	https://github.com/lxde/%{name}/archive/%{name}-%{version}.tar.xz
%endif
License:	LGPLv2.1+
Group:		Graphical desktop/Other
Url:		http://lxqt.org
Patch2:		pcmanfm-qt-0.7.0-default-background.patch
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libfm)
BuildRequires:	pkgconfig(libmenu-cache)
BuildRequires:	pkgconfig(lxqt)
BuildRequires:	pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	qmake5
Suggests:	ark
Suggests:	kde-cli-tools

%description
File manager for the LXQt desktop.

%files
%{_bindir}/pcmanfm-qt
%{_datadir}/applications/*.desktop
%{_datadir}/libfm-qt
%{_datadir}/pcmanfm-qt
%{_mandir}/man1/pcmanfm-qt.1*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	PCManFM Qt backend library
Group:		System/Libraries
Conflicts:	%{_lib}fm-qt0.0.0 < 0.7.0-2
Obsoletes:	%{_lib}fm-qt0.0.0 < 0.7.0-2
Obsoletes:	%{mklibname fm-qt5 1} < 0.9.0

%description -n %{libname}
PCManFM Qt backend library.

%files -n %{libname}
%{_libdir}/libfm-qt5.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for PCManFM
Group:		Development/C++
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for PCManFM.

%files -n %{devname}
%{_libdir}/libfm-qt5.so
%{_includedir}/libfm-qt
%{_libdir}/pkgconfig/libfm-qt5.pc

#----------------------------------------------------------------------------

%prep
%if %git
%setup -q -n %{name}-%{git}
%else
%setup -q
%endif
%apply_patches

%cmake_qt5 -G Ninja

%build
# change desktop file name and comment to distinguish it from pcmanfm
sed -i 's/File Manager/QT File Manager/' pcmanfm/pcmanfm-qt.desktop.in

# change gksu to kdesu as with gksu no icons are shown when running as root
sed -i 's|gksu %s|%{_bindir}/kdesu %s|g' pcmanfm/preferences.ui pcmanfm/settings.cpp pcmanfm/translations/pcmanfm-qt*.ts

# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8
%ninja -C build

%install
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8
%ninja_install -C build
