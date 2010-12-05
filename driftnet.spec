%define name    driftnet
%define version 0.1.6
%define release %mkrel 9
%define summary Network pictures sniffer

Summary:        %summary
Name:           %name
Version:        %version
Release:        %release
License:        GPL
Group:          Networking/Other
URL:            http://www.ex-parrot.com/~chris/driftnet/

Source0:        %name-%version.tar.bz2
#http://www.ex-parrot.com/~chris/driftnet/%name-%version.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:       libpcap-devel libjpeg-devel libungif-devel gtk-devel makedepend

%description
Inspired by EtherPEG, Driftnet is a program which listens to network traffic 
and picks out images from TCP streams it observes.

%prep
%setup -q

%build
%make

%install
rm -rf %buildroot
mkdir -p %buildroot%_bindir
cp driftnet %buildroot%_bindir

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc CHANGES COPYING CREDITS README TODO
%defattr(0755,root,root)
%_bindir/*
