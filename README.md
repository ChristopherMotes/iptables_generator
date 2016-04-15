# iptables generator
 iptables_generator uses the contents of /etc/sysconfig/iptables.d to build /etc/sysconfig/iptables.
## installation
install from yum/rpm
## Use

`/usr/sbin/iptables_generator.pl <-r>
iptables_generator.pl without options writes /etc/sysconfig/iptables
		-r	reload iptables after completion`
### acpts files
Accept files allow easy addion of IP addresses through IPtables rules. You don't need explicite knowledge of iptables to work with accepts files. <filename>.acpts will likely be ovrewitten on the next rpm update. If you need to add IPs to a defined rule, create <rule_name>.local.acpts (case matters).
#### **global_accepts.acpts**
This file allows certain IPs through on every defined port. If your project has special monitoring host, etc. create /etc/sysconfig/itables.d/global_accepts.local.acpts with the ipaddress/CIDR Network listed there.
#### **adding local accepts**
Create a file <rule name>.local.acpts and add IPs to the file
```
[christophermotes@rpmbuild-6 ~]$ cd /etc/sysconfig/iptables.d
[christophermotes@rpmbuild-6 iptables.d]$ sudo iptables -nvL ccagent  | grep 10.0.0.12
[christophermotes@rpmbuild-6 iptables.d]$ sudo -e ccagent.local.acpts
10.0.0.12
10.0.0.120
~                                                                                                                  
~                                                                                                                  
~     
wq
[christophermotes@rpmbuild-6 iptables.d]$ sudo iptables_generator.pl
[christophermotes@rpmbuild-6 iptables.d]$ sudo service iptables reload
iptables: Trying to reload firewall rules:                 [  OK  ]
[christophermotes@rpmbuild-6 iptables.d]$ sudo iptables -nvL ccagent  | grep 10.0.0.12
    0     0 ACCEPT     all  --  *      *       10.0.0.12        0.0.0.0/0           
    0     0 ACCEPT     all  --  *      *       10.0.0.120       0.0.0.0/0 
```

### rules files
Rules files define ports or protocols for iptables actions. **You must know  iptables to work with these files correctly.**
rules files managed by the rpm (rpm -ql iptables_generator) are subject to overwrite with each version of the rpm. Thus, rules files controled by the RPM shouldn't be edited.
##### **Creating a new listening port.**
```
[christophermotes@motes11  git]$ cd /etc/iptables.d 
[christophermotes@motes11 iptables.d]$ sudo perl -pe 's/snmpd/oracle/g' snmpd.rules | sudo tee oracle.rules
[christophermotes@motes11 iptables.d]$ sudo -e oracle.rules 
```
From vi edit the JUMP rules for your port or protocol change:

Begining of vi session
```
FILTER          = oracle - [0:0]
JUMP            = -A INPUT -p tcp -m tcp --dport 199 -j oracle
JUMP            = -A INPUT -p udp -m udp --dport 161 -j oracle
LOG             = -A oracle -j LOG --log-prefix "dropped_oracle_ips: "
DROP            = -A oracle -j DROP
```
End of vi session
```
FILTER          = oracle - [0:0]
JUMP            = -A INPUT -p tcp -m tcp --dport 1521 -j oracle
LOG             = -A oracle -j LOG --log-prefix "dropped_oracle_ips: "
DROP            = -A oracle -j DROP
~                                                                                                                  
~                                                                                                                  
:wq
```
With the new rules inplace execut  iptables_generator.pl and reload iptables. validate  your new with the iptables command
```
[christophermotes@rpmbuild-6 iptables.d]$ sudo -e oracle.rules 
[christophermotes@rpmbuild-6 iptables.d]$ sudo iptables_generator.pl
[christophermotes@rpmbuild-6 iptables.d]$ sudo service iptables reload
iptables: Trying to reload firewall rules:                 [  OK  ]
[christophermotes@rpmbuild-6 iptables.d]$ sudo iptables -nvL oracle
Chain oracle (1 references)
 pkts bytes target     prot opt in     out     source               destination         
    0     0 ACCEPT     all  --  *      *       10.1.62.23         0.0.0.0/0           
    0     0 ACCEPT     all  --  *      *       10.1.1.129       0.0.0.0/0           
    0     0 ACCEPT     all  --  *      *       10.1.1.1         0.0.0.0/0           
    0     0 ACCEPT     all  --  *      *       10.1.1.2         0.0.0.0/0           
<SNIP>
    0     0 ACCEPT     all  --  *      *       10.1.200.9           0.0.0.0/0           
    0     0 ACCEPT     all  --  *      *       10.1.1.65        0.0.0.0/0           
    0     0 LOG        all  --  *      *       0.0.0.0/0            0.0.0.0/0           LOG flags 0 level 4 prefix `dropped_oracle_ips: ' 
    0     0 DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0   
```
The IPs listed come from the global_accepts rule. Create oracle.local.acpts with the desired IPs (See local accpts files above).
### def files
Def files are for defaults. They should generally remain untouched
