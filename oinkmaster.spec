Summary:	A tool to update Snort rules
Summary(pl):	Narzêdzie do aktualizacji regu³ Snort'a
Name:		oinkmaster
Version:	0.6
Release:	1
License:	BSD
Vendor:		Andreas Östling <andreaso@it.su.se>
Group:		Networking
Source0:	ftp://ftp.it.su.se/pub/andreas/oinkmaster/%{name}-%{version}.tar.gz
Patch0:		%{name}-config_path.patch
URL:		http://nitzer.dhs.org/oinkmaster
Requires:	perl
Requires:	snort
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
oinkmaster helps you update your Snort rules and comment out the
unwanted ones after each update. It will tell you exactly what changed
since the last update, giving you good control of your rules.

%description -l pl
oinkmaster pomaga w aktualizowaniu regu³ Snort'a, komentuje je po
ka¿dej aktualizacji. Poinformuje cie dok³adnie co zosta³o zmienione od
ostatniej aktualizacji, otrzymasz w ten sposób dobr± kontrole na
regu³ami.

%prep
%setup -q

%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_sysconfdir}/oinkmaster,%{_bindir}}

install oinkmaster.pl $RPM_BUILD_ROOT%{_bindir}
install oinkmaster.conf $RPM_BUILD_ROOT%{_sysconfdir}/oinkmaster

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README UPGRADING ChangeLog INSTALL
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/oinkmaster/oinkmaster.conf
