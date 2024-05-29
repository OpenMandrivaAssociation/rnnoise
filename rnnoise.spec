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
# Data vesion should be with same number as in /%{name}-%{version}/model_version
Source1:	https://media.xiph.org/rnnoise/models/rnnoise_data-0b50c45.tar.gz
# PATCH https://github.com/xiph/rnnoise/issues/222
Patch0:         372f7b4.patch
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
%build
cp -p %{SOURCE1} .
autoreconf -fiv
%configure \
	--enable-examples-build

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
