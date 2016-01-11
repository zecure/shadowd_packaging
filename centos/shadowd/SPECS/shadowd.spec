Name:             shadowd
Version:          2.0.0
Release:          1%{?dist}
Summary:          Shadow Daemon web application firewall server
Group:            Applications/Internet

License:          GPLv2
URL:              https://shadowd.zecure.org/
Source0:          https://shadowd.zecure.org/files/shadowd-%{version}.tar.gz
Source1:          shadowd.service

BuildRequires:    systemd, cmake, openssl-devel, boost-devel, libdbi-devel, cryptopp-devel, jsoncpp-devel
Requires:         libdbi-dbd-mysql, libdbi-dbd-pgsql
Requires(pre):    /usr/sbin/useradd
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description
Shadow Daemon is a collection of tools to detect, record and prevent attacks
on web applications. Technically speaking, Shadow Daemon is a web application
firewall that intercepts requests and filters out malicious parameters. It is a
modular system that separates web application, analysis and interface to
increase security, flexibility and expandability. This component is the
background server that handles the analysis and storage of requests.


%prep
%setup -q


%build
%cmake .
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/shadowd.service


%pre
/usr/sbin/useradd -r -U -M -d /dev/null -s /sbin/nologin shadowd 2>/dev/null || true


%post
%systemd_post shadowd.service


%preun
%systemd_preun shadowd.service


%postun
%systemd_postun_with_restart shadowd.service


%files
%defattr(-,root,root,-)
%{_bindir}/shadowd
%dir %{_sysconfdir}/shadowd
%config(noreplace) %{_sysconfdir}/shadowd/shadowd.ini
%attr(0640,root,shadowd) %{_sysconfdir}/shadowd/shadowd.ini
%{_unitdir}/shadowd.service
%dir %{_datarootdir}/shadowd
%{_datarootdir}/shadowd/mysql_layout.sql
%{_datarootdir}/shadowd/pgsql_layout.sql
%{_datarootdir}/shadowd/mysql_layout_1.0.0-1.1.0.sql
%{_datarootdir}/shadowd/pgsql_layout_1.0.0-1.1.0.sql
%{_datarootdir}/shadowd/mysql_layout_1.1.3-2.0.0.sql
%{_datarootdir}/shadowd/pgsql_layout_1.1.3-2.0.0.sql
%doc %{_mandir}/man1/shadowd.1.gz


%changelog
* Mon Jan 11 2016 Hendrik Buchwald <hb@zecure.org> - 2.0.0-1
- New major version

* Sat May 16 2015 Hendrik Buchwald <hb@zecure.org> - 1.1.3-1
- Bug fix in the storage queue and flood protection

* Sat May 02 2015 Hendrik Buchwald <hb@zecure.org> - 1.1.2-1
- Uncritical patches to improve performance and reliability

* Thu Mar 26 2015 Hendrik Buchwald <hb@zecure.org> - 1.1.0-1
- Performance and signature updates

* Sat Jan 24 2015 Hendrik Buchwald <hb@zecure.org> - 1.0.0-1
- Initial version of the package
