%define		cvs	20040426cvs

Summary:	Network pictures sniffer
Name:		driftnet
Version:	0.1.6
Release:	10.%{cvs}.1
License:	GPL
Group:		Networking/Other
URL:		https://www.ex-parrot.com/~chris/driftnet/
Source0:	%{name}-%{version}-%{cvs}.tar.gz
Source1:	driftnet-0.1.6-pam.config
Source2:	driftnet-0.1.6-security.config
Patch0:		driftnet-0.1.6-libpng.patch
Patch1:		driftnet-0.1.6-avoid-tmpname.patch
Patch2:		driftnet-0.1.6-no-makedepend.patch
Patch3:		driftnet-0.1.6-linkage.patch
BuildRequires:	libpcap-devel
BuildRequires:	jpeg-devel
BuildRequires:	ungif-devel
BuildRequires:	pkgconfig(gtk+-2.0)

%description
Inspired by EtherPEG, Driftnet is a program which listens to network traffic
and picks out images from TCP streams it observes.

%prep
%setup -q -n %{name}-%{version}-%{cvs}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%make

%install
mkdir -p %{buildroot}%{_bindir}
install -Dpm 0755 driftnet %{buildroot}%{_sbindir}/driftnet
install -Dpm 0644 driftnet.1 %{buildroot}%{_mandir}/man1/driftnet.1
ln -sf consolehelper %{buildroot}%{_bindir}/driftnet
install -Dpm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/driftnet
install -Dpm 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/security/console.apps/driftnet

%files
%doc CHANGES COPYING CREDITS README TODO
%{_bindir}/driftnet
%{_sbindir}/driftnet
%config(noreplace) %{_sysconfdir}/pam.d/driftnet
%config %{_sysconfdir}/security/console.apps/driftnet
%{_mandir}/man1/driftnet.1*

