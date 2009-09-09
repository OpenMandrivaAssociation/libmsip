%define name	libmsip
%define oname	msip
%define version 0.3.1
%define svn	3565
%define release %mkrel %svn.2

%define major	0
%define libname %mklibname %{oname} %major
%define develname %mklibname %{oname} -d

Name: 	 	%{name}
Summary: 	SIP library from MiniSip
Version: 	%{version}
Release: 	%{release}

Source:		http://www.minisip.org/source/%{name}-%{svn}.tar.bz2
URL:		http://www.minisip.org/
License:	GPL
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libmutil-devel >= 0.3.1-3565.0
BuildRequires:	libmnetutil-devel >= 0.3.1-3565.0
BuildRequires:	libmcrypto-devel >= 0.3.1-3565.0

%description
SIP library from MiniSip

%package -n 	%{libname}
Summary:        Dynamic libraries from %name
Group:          System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
Dynamic libraries from %name.

%package -n 	%{develname}
Summary: 	Header files and static libraries from %name
Group: 		Development/C
Requires: 	%{libname} >= %{version}
Provides:	%{name}-devel = %{version}-%{release} 

%description -n %{develname}
Libraries and includes files for developing programs based on %name.

%prep
%setup -q -n %name

%build
./bootstrap
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
#cp include/%name/SipTransactionNon* %buildroot/%_includedir/%name/

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README 
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la


