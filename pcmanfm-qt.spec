%define major 0
%define libname %mklibname fm-qt %{major}
%define devname %mklibname fm-qt -d

Summary:	File manager for the LXQt desktop
Name:		pcmanfm-qt
Version:	0.7.0
Release:	2
License:	LGPLv2.1+
Group:		Graphical desktop/Other
Url:		http://lxqt.org
Source0:	http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
Patch0:		pcmanfm-qt-0.7.0-soname.patch
Patch1:		pcmanfm-qt-0.7.0-cxxflags.patch
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libfm)
BuildRequires:	pkgconfig(libmenu-cache)
BuildRequires:	pkgconfig(lxqt)
BuildRequires:	pkgconfig(x11)

%description
File manager for the LXQt desktop.

%files
%{_bindir}/pcmanfm-qt
%{_datadir}/applications/*.desktop

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	PCManFM Qt backend library
Group:		System/Libraries
Conflicts:	%{_lib}fm-qt0.0.0 < 0.7.0-2
Obsoletes:	%{_lib}fm-qt0.0.0 < 0.7.0-2

%description -n %{libname}
PCManFM Qt backend library.

%files -n %{libname}
%{_libdir}/libfm-qt.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for PCManFM
Group:		Development/C++
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for PCManFM.

%files -n %{devname}
%{_libdir}/libfm-qt.so
%{_includedir}/libfm-qt
%{_libdir}/pkgconfig/libfm-qt.pc

#----------------------------------------------------------------------------

%prep
%setup -q -c %{name}-%{version}
%patch0 -p1
%patch1 -p1

%build
%cmake
%make

%install
%makeinstall_std -C build

