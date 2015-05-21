# $Id: snortalog.spec 1833 2004-08-02 23:22:28Z dag $
# Authority: dag
# Upstream: Jeremy Chartier <jeremy,chartier$free,fr>
# Based on rpm of Dag Wieers <dag@wieers.com> - ag Apt Repository, http://dag.wieers.com/apt/

Summary: Snort log analyzer
Name: snortalog
Version: 0.0.1
Release: 1%{?dist}
License: GPL
URL: http://jeremy.chartier.free.fr/snortalog/
Source: %{name}-%{version}.tar.gz

BuildRequires: perl
Requires: perl
BuildArch: noarch
Autoreq: no

%description
SnortALog is a powerfull perl script that summarizes snort logs making
it easy to view any attacks against your network.

SnortALog works with all versions of SNORT and is the only script who
can analyse snort's logs in all formats (Syslog, Fast and Full alerts).
Also, it is able to summarize Fw-1 (NG and 4.1), Netfilter and IPFilter
logs in a simmilar way.

%prep
%setup

%build

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

%files
%defattr(-,root,root)
%attr(0755,root,root) /usr/share/snortalog/snortalog.pl
/usr/share/snortalog/

%changelog
