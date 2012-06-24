%include	/usr/lib/rpm/macros.perl
Summary:	A tool to update Snort rules
Summary(pl):	Narz�dzie do aktualizacji regu� Snorta
Name:		oinkmaster
Version:	1.1
Release:	1
License:	BSD
Group:		Networking
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	28cfaf6220f5fc3fa3f3838ea33cecf1
Patch0:		%{name}-config_path.patch
URL:		http://oinkmaster.sourceforge.net/
BuildRequires:	rpm-perlprov
Requires:	snort
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
oinkmaster helps you update your Snort rules and comment out the
unwanted ones after each update. It will tell you exactly what changed
since the last update, giving you good control of your rules.

%description -l pl
oinkmaster pomaga w aktualizowaniu regu� Snorta, zakomentowuj�c
niechciane regu�y po ka�dej aktualizacji. Poinformuje dok�adnie co
zosta�o zmienione od ostatniej aktualizacji, daj�c dobr� kontrol� nad
regu�ami.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/oinkmaster,%{_bindir}}

install oinkmaster.pl $RPM_BUILD_ROOT%{_bindir}
install oinkmaster.conf $RPM_BUILD_ROOT%{_sysconfdir}/oinkmaster

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README UPGRADING ChangeLog INSTALL
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}/oinkmaster
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/oinkmaster/oinkmaster.conf
