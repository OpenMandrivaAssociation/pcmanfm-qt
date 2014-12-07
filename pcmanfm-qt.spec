%define major 1
%define libname %mklibname fm-qt5 %{major}
%define devname %mklibname fm-qt5 -d
%define git 0

Summary:	File manager for the LXQt desktop
Name:		pcmanfm-qt
Version:	0.8.0
%if %git
Release:	0.%git.1
Source0:	%{name}-%{git}.tar.xz
%else
Release:	2
Source0:	http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
%endif
License:	LGPLv2.1+
Group:		Graphical desktop/Other
Url:		http://lxqt.org
Patch2:		pcmanfm-qt-0.7.0-default-background.patch
BuildRequires:	cmake
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libfm)
BuildRequires:	pkgconfig(libmenu-cache)
BuildRequires:	pkgconfig(lxqt-qt5)
BuildRequires:	pkgconfig(x11)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	qmake5

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

%build
%cmake -DUSE_QT5:BOOL=ON
%make

%install
%makeinstall_std -C build

