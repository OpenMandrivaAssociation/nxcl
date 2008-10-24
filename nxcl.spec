%define name    nxcl
%define version 0.9
%define release %mkrel 0.%revision.2
%define revision 519

%define __libtoolize    /bin/true

Summary:       A library for building NX clients
Name:          %{name}
Version:       %{version}
Release:       %{release}
License:       GPL
Url:           http://freenx.berlios.de/
Group:         Graphical desktop/KDE
Source:        %{name}-%{version}-svn%{revision}.tar.bz2
Patch0:		   nxcl-fixdocdir.patch
BuildRoot:     %{_tmppath}/%{name}-%{version}
BuildRequires: libx11-devel dbus-devel doxygen
Epoch:		   1

%description
A library for building NX clients

%prep
%setup -n %{name}
%patch0 -p1 

%build
autoreconf -is
%configure

%make

%install
rm -Rf %{buildroot}
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/libtest
%{_bindir}/notQttest
%{_bindir}/nxcl
%{_bindir}/nxcmd
%{_libdir}/lib*nxcl*
%{_libdir}/pkgconfig/nxcl.pc
%{_includedir}/nxcl
%{_includedir}/nxcl/*
%{_docdir}/nxcl*
