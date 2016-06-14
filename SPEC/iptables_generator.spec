%global source_dir  %{_datadir}/%{name}-source
Name:           iptables_generator
Version:        1.0.0
Release:        0%{?dist}
Summary:        configures IP tables
Group:          System Environment/Libraries
License:        Commercial
#Source:         https://github/ChristopherMotes/iptables_generator/repository/archive.tar.gz
Source:         https://github.com/ChristopherMotes/iptables_generator/archive/master.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

%description
Provides a perl script with a .d like function for iptables configuration.

%prep
%setup -n %{name}-master

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
install -m 755 -d $RPM_BUILD_ROOT/etc/sysconfig/iptables.d
install -m 755 -d $RPM_BUILD_ROOT/usr/local/sbin/
install -m 755 bin/iptables_generator.pl $RPM_BUILD_ROOT/usr/local/sbin/
install -m 644 iptables.d/default_filters.def $RPM_BUILD_ROOT/etc/sysconfig/iptables.d/
install -m 644 iptables.d/default_rules.def $RPM_BUILD_ROOT/etc/sysconfig/iptables.d/
install -m 644 iptables.d/default_rules.def $RPM_BUILD_ROOT/etc/sysconfig/iptables.d/
install -m 644 iptables.d/global_accepts.acpts $RPM_BUILD_ROOT/etc/sysconfig/iptables.d/
install -m 644 iptables.d/icmp.acpts $RPM_BUILD_ROOT/etc/sysconfig/iptables.d/
install -m 644 iptables.d/icmp.rules $RPM_BUILD_ROOT/etc/sysconfig/iptables.d/
install -m 644 iptables.d/netbackup.acpts $RPM_BUILD_ROOT/etc/sysconfig/iptables.d/
install -m 644 iptables.d/netbackup.rules $RPM_BUILD_ROOT/etc/sysconfig/iptables.d/
install -m 644 iptables.d/nrpe.acpts $RPM_BUILD_ROOT/etc/sysconfig/iptables.d/
install -m 644 iptables.d/nrpe.rules $RPM_BUILD_ROOT/etc/sysconfig/iptables.d/
install -m 644 iptables.d/ntpd.acpts $RPM_BUILD_ROOT/etc/sysconfig/iptables.d/
install -m 644 iptables.d/ntpd.rules $RPM_BUILD_ROOT/etc/sysconfig/iptables.d/
install -m 644 iptables.d/snmpd.acpts $RPM_BUILD_ROOT/etc/sysconfig/iptables.d/
install -m 644 iptables.d/snmpd.rules $RPM_BUILD_ROOT/etc/sysconfig/iptables.d/
install -m 644 iptables.d/sshd.acpts $RPM_BUILD_ROOT/etc/sysconfig/iptables.d/
install -m 644 iptables.d/sshd.rules $RPM_BUILD_ROOT/etc/sysconfig/iptables.d/
install -m 644 iptables.d/sysedge.acpts $RPM_BUILD_ROOT/etc/sysconfig/iptables.d/
install -m 644 iptables.d/sysedge.rules $RPM_BUILD_ROOT/etc/sysconfig/iptables.d/

%files
%defattr(-,root,root)
%dir /etc/sysconfig/iptables.d
/usr/local/sbin/iptables_generator.pl
/etc/sysconfig/iptables.d/cam.rules
/etc/sysconfig/iptables.d/ccagent.rules
/etc/sysconfig/iptables.d/default_filters.def
/etc/sysconfig/iptables.d/default_rules.def
/etc/sysconfig/iptables.d/encase.rules
/etc/sysconfig/iptables.d/global_accepts.acpts
/etc/sysconfig/iptables.d/icmp.acpts
/etc/sysconfig/iptables.d/icmp.rules
/etc/sysconfig/iptables.d/netbackup.acpts
/etc/sysconfig/iptables.d/netbackup.rules
/etc/sysconfig/iptables.d/nrpe.acpts
/etc/sysconfig/iptables.d/nrpe.rules
/etc/sysconfig/iptables.d/ntpd.acpts
/etc/sysconfig/iptables.d/ntpd.rules
/etc/sysconfig/iptables.d/snmpd.acpts
/etc/sysconfig/iptables.d/snmpd.rules
/etc/sysconfig/iptables.d/sshd.acpts
/etc/sysconfig/iptables.d/sshd.rules
/etc/sysconfig/iptables.d/sysedge.acpts
/etc/sysconfig/iptables.d/sysedge.rules

%changelog
* Fri Feb 26 2016 Christopher Motes <christopher.motes@motes.gov> - %{name}-1.0.2
- missing encase
* Fri Feb 26 2016 Christopher Motes <christopher.motes@motes.gov> - %{name}-1.0.0
- Initial build
