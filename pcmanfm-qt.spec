Summary:	File manager for the LXQt desktop
Name:		pcmanfm-qt
Version:	2.1.0
Release:	%{?git:0.%git.}4
Source0:	https://github.com/lxqt/pcmanfm-qt/releases/download/%{version}/pcmanfm-qt-%{version}.tar.xz
License:	LGPLv2.1+
Group:		Graphical desktop/Other
Url:		https://lxqt.org
Patch0:		pcmanfm-qt-0.12.0-omv-settings.patch
Patch1:		pcmanfm-qt-0.7.0-default-background.patch
Patch2:		pcmanfm-qt-settings.patch
BuildSystem:	cmake
BuildOption:	-DPULL_TRANSLATIONS:BOOL=OFF
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
%{_datadir}/polkit-1/actions/com.github.lxqt.pcmanfm-qt.policy

#----------------------------------------------------------------------------

%build -p
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8

%install -p
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8

%install -a
mkdir -p %{buildroot}%{_datadir}/polkit-1/actions
cat >%{buildroot}%{_datadir}/polkit-1/actions/com.github.lxqt.pcmanfm-qt.policy <<'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!-- SPDX-FileCopyrightText: no
     SPDX-License-Identifier: CC0-1.0
-->
<!DOCTYPE policyconfig PUBLIC
"-//freedesktop//DTD PolicyKit Policy Configuration 1.0//EN"
"http://www.freedesktop.org/standards/PolicyKit/1/policyconfig.dtd">
<policyconfig>

 <vendor>Dolphin</vendor>
 <vendor_url>https://apps.kde.org/dolphin</vendor_url>

 <action id="com.github.lxqt.pcmanfm-qt.pkexec.run">
    <description>PCManFM-Qt file manager</description>
    <message>Authentication is required to run the PCManFM-Qt file manager in admin mode</message>
    <icon_name>pcmanfm-qt</icon_name>
    <defaults>
     <allow_any>no</allow_any>
     <allow_inactive>no</allow_inactive>
     <allow_active>auth_admin</allow_active>
    </defaults>
    <annotate key="org.freedesktop.policykit.exec.path">%{_bindir}/pcmanfm-qt</annotate>
    <annotate key="org.freedesktop.policykit.exec.allow_gui">true</annotate>
 </action>
</policyconfig>
EOF
