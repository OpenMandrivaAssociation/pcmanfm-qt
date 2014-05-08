%define debug_package %{nil}
%define libname %mklibname fm-qt 0.0.0
%define devname %mklibname -d fm-qt

Name: pcmanfm-qt
Version: 0.7.0
Release: 1
Source0: http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
Summary: File manager for the LXQt desktop
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake
BuildRequires: cmake(lxqt)
BuildRequires: qt4-devel
BuildRequires: pkgconfig(libfm)
BuildRequires: pkgconfig(libmenu-cache)

%description
File manager for the LXQt desktop

%package -n %{libname}
Summary: PCManFM Qt backend library
Group: System/Libraries

%description -n %{libname}
PCManFM Qt backend library

%package -n %{devname}
Summary: Development files for PCManFM
Group: Development/C

%description -n %{devname}
Development files for PCManFM

%prep
%setup -q -c %{name}-%{version}
%cmake

%build
%make -C build

%install
%makeinstall_std -C build

%files
%{_bindir}/pcmanfm-qt
%{_datadir}/applications/*.desktop

%files -n %{libname}
%{_libdir}/libfm-qt.so.0.0.0

%files -n %{devname}
%{_libdir}/libfm-qt.so
%{_includedir}/libfm-qt
%{_libdir}/pkgconfig/libfm-qt.pc
