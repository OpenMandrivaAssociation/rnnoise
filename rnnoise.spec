%define major 0
%define libname	%mklibname rnnoise %{major}
%define devname	%mklibname -d rnnoise 

Summary:	Recurrent neural network for audio noise reduction
Name:		rnnoise
Version:	0.2
Release:	1
License:	BSD
Group:		System/Libraries
# also https://github.com/xiph/rnnoise
Url:		https://gitlab.xiph.org/xiph/rnnoise
Source0:	https://gitlab.xiph.org/xiph/rnnoise/-/archive/v%{version}/rnnoise-v%{version}.tar.bz2
BuildRequires:	autoconf automake libtool make
BuildRequires:	doxygen graphviz
BuildRequires:	gettext

%description
%summary

%package -n	%{libname}
Summary:	%summary
Group:		System/Libraries

%description -n	%{libname}
%summary

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}

%description -n	%{devname}
This package includes the development files for %{name}.

%prep
%autosetup -n %{name}-v%{version} -p1
autoreconf -fiv
%configure \
	--enable-examples-build

%build
%make_build

%install
%make_install
rm -f %{buildroot}%{_datadir}/doc/%{name}/AUTHORS
rm -f %{buildroot}%{_datadir}/doc/%{name}/README
rm -f %{buildroot}%{_datadir}/doc/%{name}/COPYING

%files -n %{libname}
%{_libdir}/librnnoise.so.%{major}*

%files -n %{devname}
%{_includedir}/rnnoise.h
%{_libdir}/librnnoise.so
%{_libdir}/pkgconfig/rnnoise.pc
%{_docdir}/rnnoise
