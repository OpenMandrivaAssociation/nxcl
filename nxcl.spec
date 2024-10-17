%define name    nxcl
%define version 0.9
%define release %mkrel 0.%revision.5
%define revision 631

%define __libtoolize    /bin/true

Summary:       A library for building NX clients
Name:          %{name}
Version:       %{version}
Release:       %{release}
License:       GPL
Url:           https://freenx.berlios.de/
Group:         Graphical desktop/KDE
Source0:        %{name}-%{version}-svn%{revision}.tar.bz2
Patch0:		   nxcl-fixdocdir.patch
Patch1:        nxcl-fixbuild.patch
Patch2:		nxcl-gcc47.patch
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(x11)
BuildRequires: doxygen
Epoch:		   1

%description
A library for building NX clients

%prep
%setup -n %{name}
#%patch0 -p1 
%patch1 -p1
%patch2 -p0

%build
sed -i -e "s#1.0#0.9#" configure.ac || die "version sed failed"


autoreconf -is
%configure

%make

%install
%makeinstall

%files
%{_bindir}/libtest
%{_bindir}/notQttest
%{_bindir}/nxcl
%{_bindir}/nxcmd
%{_libdir}/lib*nxcl*
%{_libdir}/pkgconfig/nxcl.pc
%{_includedir}/nxcl/*
%{_docdir}/nxcl*
