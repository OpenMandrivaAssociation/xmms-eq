%define name    xmms-eq
%define version 0.6
%define release %mkrel 9

Summary: Equalizer plugin for XMMS
Name: %{name}
Version: %{version}
Release: %{release}
Group: Sound
URL: http://equ.sourceforge.net/ 
Source: http://prdownloads.sourceforge.net/equ/eq-xmms-%{version}.tar.bz2 
Patch: eq-xmms-0.6-no-autodetect.patch
License: GPLv2+
Requires: xmms >= 1.0.1
BuildRequires: xmms-devel 
BuildRequires: xmms
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
EQU is a realtime graphical equalizer effect plugin that will equalize
almost everything that you play through XMMS, not just the MP3s.

%prep

%setup -q -n eq-xmms-%{version}/
%patch -p1 -b .auto
libtoolize --force
aclocal
autoconf
automake

%build

%configure2_5x --libdir=%_libdir/xmms/Effect/ \
%ifarch x86_64
--enable-sse2
%endif

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot%_libdir/xmms/Effect/libeq.la
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS README TODO NEWS ChangeLog BUGS 
%{_libdir}/xmms/Effect/libeq.so


