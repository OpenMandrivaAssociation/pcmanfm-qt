Summary:	File manager for the LXQt desktop
Name:		pcmanfm-qt
Version:	1.4.1
Release:	%{?git:1.%git.}1
Source0:	https://github.com/lxqt/pcmanfm-qt/releases/download/%{version}/pcmanfm-qt-%{version}.tar.xz
License:	LGPLv2.1+
Group:		Graphical desktop/Other
Url:		http://lxqt.org
Patch0:		pcmanfm-qt-0.12.0-omv-settings.patch
Patch1:		pcmanfm-qt-0.7.0-default-background.patch
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libfm)
BuildRequires:	pkgconfig(libfm-extra)
BuildRequires:	pkgconfig(libmenu-cache)
BuildRequires:	pkgconfig(lxqt)
BuildRequires:	pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	pkgconfig(libfm-qt) >= 0.12.0
BuildRequires:	cmake(lxqt-build-tools)
BuildRequires:	qmake5
Suggests:	ark
Suggests:	lxqt-sudo

%description
File manager for the LXQt desktop.

%files
%{_bindir}/pcmanfm-qt
%{_datadir}/applications/*.desktop
%{_datadir}/pcmanfm-qt
%{_mandir}/man1/pcmanfm-qt.1*
%{_sysconfdir}/xdg/autostart/lxqt-desktop.desktop
%{_datadir}/icons/hicolor/*/apps/pcmanfm-qt.*

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_qt5 -DPULL_TRANSLATIONS=NO -G Ninja

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
