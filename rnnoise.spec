%define major 0
%define libname	%mklibname rnnoise %{major}
%define devname	%mklibname -d rnnoise 

Summary:	Recurrent neural network for audio noise reduction
Name:		rnnoise
Version:	0.0.1
Release:	1
License:	AsIs
Group:		System/Libraries
Url:		http://libusb.info
Source0:	https://github.com/xiph/rnnoise/archive/rnnoise-master.zip

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
%setup -q -n %{name}-master
autoreconf -fiv

%build
%configure \
	--disable-static \
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
