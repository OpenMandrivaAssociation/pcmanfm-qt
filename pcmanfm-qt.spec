%define git 0

Summary:	File manager for the LXQt desktop
Name:		pcmanfm-qt
Version:	0.11.2
%if %git
Release:	0.%git.1
Source0:	%{name}-%{git}.tar.xz
%else
Release:	1
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
BuildRequires:	cmake(fm-qt)
BuildRequires:	cmake(lxqt-build-tools)
BuildRequires:	qmake5
BuildRequires:	git-core
Suggests:	ark
Suggests:	lxqt-sudo

%description
File manager for the LXQt desktop.

%files
%{_bindir}/pcmanfm-qt
%{_datadir}/applications/*.desktop
%{_datadir}/pcmanfm-qt
%{_mandir}/man1/pcmanfm-qt.1*

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
