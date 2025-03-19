Summary:	File manager for the LXQt desktop
Name:		pcmanfm-qt
Version:	2.1.0
Release:	%{?git:0.%git.}3
Source0:	https://github.com/lxqt/pcmanfm-qt/releases/download/%{version}/pcmanfm-qt-%{version}.tar.xz
License:	LGPLv2.1+
Group:		Graphical desktop/Other
Url:		https://lxqt.org
Patch0:		pcmanfm-qt-0.12.0-omv-settings.patch
Patch1:		pcmanfm-qt-0.7.0-default-background.patch
Patch2:		pcmanfm-qt-settings.patch
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
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(LayerShellQt)
BuildRequires:	pkgconfig(libfm-qt6) >= 0.12.0
BuildRequires:	cmake(lxqt2-build-tools)
Suggests:	ark
Suggests:	lxqt-sudo

Requires: gvfs

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
%cmake -DPULL_TRANSLATIONS=NO -G Ninja

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
