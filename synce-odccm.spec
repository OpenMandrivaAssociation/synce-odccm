%define name	synce-odccm
%define shortname odccm
%define release  %mkrel 6
%define version  0.10.0

%define major 0

%define libname %mklibname %shortname %major

Summary:	SynCE: Communication application
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	MIT
Group:		System/Libraries
Source:		%{shortname}-%{version}.tar.bz2
#(eandry) Add a valid dbus configuration
Patch0:		synce-odccm-0.10.0-dbus-conf.patch
URL:		https://synce.sourceforge.net/
Buildroot:	%{_tmppath}/%name-root
BuildRequires:	libsynce-devel = %{version}
BuildRequires:	hal-devel gob2 glib2-devel libgnet2-devel
BuildRequires:	libdbus-glib-devel
Obsoletes:	%libname
Obsoletes:	%libname-devel
Conflicts:	synce-kde < 0.9.1-2

%description
%{shortname} is part of the SynCE project:

%prep
%setup -q -n %{shortname}-%{version}
%patch0

%build
%configure2_5x --with-libsynce=%{_prefix}
%make

%install
rm -rf %buildroot
%makeinstall_std

%files
%defattr(-,root,root)
%doc README
%{_sbindir}/*
%{_mandir}/man1/*
