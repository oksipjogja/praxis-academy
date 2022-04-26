## install MariaDB
"""
    donie@donie-ThinkPad-T430:~/praxis-academy/kemampuan-dasar/kemampuan-dasar-2/minggu-4$ sudo apt install mariadb-server
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  galera-3 libconfig-inifiles-perl libdbd-mysql-perl libdbi-perl libhtml-template-perl libterm-readkey-perl
  mariadb-client-10.3 mariadb-client-core-10.3 mariadb-common mariadb-server-10.3 mariadb-server-core-10.3 socat
Suggested packages:
  libmldbm-perl libnet-daemon-perl libsql-statement-perl libipc-sharedcache-perl mailx mariadb-test tinyca
The following NEW packages will be installed:
  galera-3 libconfig-inifiles-perl libdbd-mysql-perl libdbi-perl libhtml-template-perl libterm-readkey-perl
  mariadb-client-10.3 mariadb-client-core-10.3 mariadb-common mariadb-server mariadb-server-10.3
  mariadb-server-core-10.3 socat
0 upgraded, 13 newly installed, 0 to remove and 0 not upgraded.
Need to get 19,4 MB of archives.
After this operation, 164 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://archive.ubuntu.com/ubuntu focal-updates/universe amd64 mariadb-common all 1:10.3.34-0ubuntu0.20.04.1 [15,9 kB]
Get:2 http://archive.ubuntu.com/ubuntu focal/universe amd64 galera-3 amd64 25.3.29-1 [898 kB]
Get:3 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 libdbi-perl amd64 1.643-1ubuntu0.1 [730 kB]
Get:4 http://archive.ubuntu.com/ubuntu focal/main amd64 libconfig-inifiles-perl all 3.000002-1 [40,6 kB]
Get:5 http://archive.ubuntu.com/ubuntu focal-updates/universe amd64 mariadb-client-core-10.3 amd64 1:10.3.34-0ubuntu0.20.04.1 [5.853 kB]
Get:6 http://archive.ubuntu.com/ubuntu focal-updates/universe amd64 mariadb-client-10.3 amd64 1:10.3.34-0ubuntu0.20.04.1 [1.130 kB]
Get:7 http://archive.ubuntu.com/ubuntu focal-updates/universe amd64 mariadb-server-core-10.3 amd64 1:10.3.34-0ubuntu0.20.04.1 [6.026 kB]
Get:8 http://archive.ubuntu.com/ubuntu focal/main amd64 socat amd64 1.7.3.3-2 [323 kB]                              
Get:9 http://archive.ubuntu.com/ubuntu focal-updates/universe amd64 mariadb-server-10.3 amd64 1:10.3.34-0ubuntu0.20.04.1 [4.204 kB]
Get:10 http://archive.ubuntu.com/ubuntu focal/universe amd64 libdbd-mysql-perl amd64 4.050-3 [82,8 kB]              
Get:11 http://archive.ubuntu.com/ubuntu focal/main amd64 libhtml-template-perl all 2.97-1 [59,0 kB]                 
Get:12 http://archive.ubuntu.com/ubuntu focal/main amd64 libterm-readkey-perl amd64 2.38-1build1 [24,6 kB]          
Get:13 http://archive.ubuntu.com/ubuntu focal-updates/universe amd64 mariadb-server all 1:10.3.34-0ubuntu0.20.04.1 [12,7 kB]
Fetched 19,4 MB in 24s (813 kB/s)                                                                                   
debconf: unable to initialize frontend: Dialog
debconf: (Dialog frontend requires a screen at least 13 lines tall and 31 columns wide.)
debconf: falling back to frontend: Readline
Preconfiguring packages ...
Selecting previously unselected package mariadb-common.
(Reading database ... 380711 files and directories currently installed.)
Preparing to unpack .../0-mariadb-common_1%3a10.3.34-0ubuntu0.20.04.1_all.deb ...
Unpacking mariadb-common (1:10.3.34-0ubuntu0.20.04.1) ...
Selecting previously unselected package galera-3.
Preparing to unpack .../1-galera-3_25.3.29-1_amd64.deb ...
Unpacking galera-3 (25.3.29-1) ...
Selecting previously unselected package libdbi-perl:amd64.
Preparing to unpack .../2-libdbi-perl_1.643-1ubuntu0.1_amd64.deb ...
Unpacking libdbi-perl:amd64 (1.643-1ubuntu0.1) ...
Selecting previously unselected package libconfig-inifiles-perl.
Preparing to unpack .../3-libconfig-inifiles-perl_3.000002-1_all.deb ...
Unpacking libconfig-inifiles-perl (3.000002-1) ...
Selecting previously unselected package mariadb-client-core-10.3.
Preparing to unpack .../4-mariadb-client-core-10.3_1%3a10.3.34-0ubuntu0.20.04.1_amd64.deb ...
Unpacking mariadb-client-core-10.3 (1:10.3.34-0ubuntu0.20.04.1) ...
Selecting previously unselected package mariadb-client-10.3.
Preparing to unpack .../5-mariadb-client-10.3_1%3a10.3.34-0ubuntu0.20.04.1_amd64.deb ...
Unpacking mariadb-client-10.3 (1:10.3.34-0ubuntu0.20.04.1) ...
Selecting previously unselected package mariadb-server-core-10.3.
Preparing to unpack .../6-mariadb-server-core-10.3_1%3a10.3.34-0ubuntu0.20.04.1_amd64.deb ...
Unpacking mariadb-server-core-10.3 (1:10.3.34-0ubuntu0.20.04.1) ...
Selecting previously unselected package socat.
Preparing to unpack .../7-socat_1.7.3.3-2_amd64.deb ...
Unpacking socat (1.7.3.3-2) ...
Setting up mariadb-common (1:10.3.34-0ubuntu0.20.04.1) ...
update-alternatives: using /etc/mysql/mariadb.cnf to provide /etc/mysql/my.cnf (my.cnf) in auto mode
Selecting previously unselected package mariadb-server-10.3.
(Reading database ... 381076 files and directories currently installed.)
Preparing to unpack .../mariadb-server-10.3_1%3a10.3.34-0ubuntu0.20.04.1_amd64.deb ...
debconf: unable to initialize frontend: Dialog
debconf: (Dialog frontend requires a screen at least 13 lines tall and 31 columns wide.)
debconf: falling back to frontend: Readline
Unpacking mariadb-server-10.3 (1:10.3.34-0ubuntu0.20.04.1) ...
Selecting previously unselected package libdbd-mysql-perl:amd64.
Preparing to unpack .../libdbd-mysql-perl_4.050-3_amd64.deb ...
Unpacking libdbd-mysql-perl:amd64 (4.050-3) ...
Selecting previously unselected package libhtml-template-perl.
Preparing to unpack .../libhtml-template-perl_2.97-1_all.deb ...
Unpacking libhtml-template-perl (2.97-1) ...
Selecting previously unselected package libterm-readkey-perl.
Preparing to unpack .../libterm-readkey-perl_2.38-1build1_amd64.deb ...
Unpacking libterm-readkey-perl (2.38-1build1) ...
Selecting previously unselected package mariadb-server.
Preparing to unpack .../mariadb-server_1%3a10.3.34-0ubuntu0.20.04.1_all.deb ...
Unpacking mariadb-server (1:10.3.34-0ubuntu0.20.04.1) ...
Setting up libconfig-inifiles-perl (3.000002-1) ...
Setting up libhtml-template-perl (2.97-1) ...
Setting up socat (1.7.3.3-2) ...
Setting up mariadb-server-core-10.3 (1:10.3.34-0ubuntu0.20.04.1) ...
Setting up galera-3 (25.3.29-1) ...
Setting up mariadb-client-core-10.3 (1:10.3.34-0ubuntu0.20.04.1) ...
Setting up libterm-readkey-perl (2.38-1build1) ...
Setting up libdbi-perl:amd64 (1.643-1ubuntu0.1) ...
Setting up mariadb-client-10.3 (1:10.3.34-0ubuntu0.20.04.1) ...
Setting up libdbd-mysql-perl:amd64 (4.050-3) ...
Setting up mariadb-server-10.3 (1:10.3.34-0ubuntu0.20.04.1) ...
debconf: unable to initialize frontend: Dialog
debconf: (Dialog frontend requires a screen at least 13 lines tall and 31 columns wide.)
debconf: falling back to frontend: Readline
Created symlink /etc/systemd/system/mysql.service → /lib/systemd/system/mariadb.service.
Created symlink /etc/systemd/system/mysqld.service → /lib/systemd/system/mariadb.service.
Created symlink /etc/systemd/system/multi-user.target.wants/mariadb.service → /lib/systemd/system/mariadb.service.
Setting up mariadb-server (1:10.3.34-0ubuntu0.20.04.1) ...
Processing triggers for systemd (245.4-4ubuntu3.16) ...
Processing triggers for man-db (2.9.1-1) ...
Processing triggers for doc-base (0.10.9) ...
Processing 1 added doc-base file...
"""
"""
donie@donie-ThinkPad-T430:~/praxis-academy/kemampuan-dasar/kemampuan-dasar-2/minggu-4$ sudo systemctl start mariadb
donie@donie-ThinkPad-T430:~/praxis-academy/kemampuan-dasar/kemampuan-dasar-2/minggu-4$ sudo systemctl enable mariadb
donie@donie-ThinkPad-T430:~/praxis-academy/kemampuan-dasar/kemampuan-dasar-2/minggu-4$ sudo systemctl status mariadb
● mariadb.service - MariaDB 10.3.34 database server
     Loaded: loaded (/lib/systemd/system/mariadb.service; enabled; vendor preset: enabled)
     Active: active (running) since Mon 2022-04-25 16:41:43 WIB; 2min 39s ago
       Docs: man:mysqld(8)
             https://mariadb.com/kb/en/library/systemd/
   Main PID: 37036 (mysqld)
     Status: "Taking your SQL requests now..."
     Tasks: 31 (limit: 11485)
     Memory: 65.7M
     CGroup: /system.slice/mariadb.service
             └─37036 /usr/sbin/mysqld

Apr 25 16:41:42 donie-ThinkPad-T430 systemd[1]: Starting MariaDB 10.3.34 database server...
Apr 25 16:41:43 donie-ThinkPad-T430 mysqld[37036]: 2022-04-25 16:41:43 0 [Note] /usr/sbin/mysqld (mysqld 10.3.34-Mar>
Apr 25 16:41:43 donie-ThinkPad-T430 systemd[1]: Started MariaDB 10.3.34 database server.
Apr 25 16:41:43 donie-ThinkPad-T430 /etc/mysql/debian-start[37074]: Looking for 'mysql' as: /usr/bin/mysql
Apr 25 16:41:43 donie-ThinkPad-T430 /etc/mysql/debian-start[37074]: Looking for 'mysqlcheck' as: /usr/bin/mysqlcheck
Apr 25 16:41:43 donie-ThinkPad-T430 /etc/mysql/debian-start[37074]: This installation of MariaDB is already upgraded>
Apr 25 16:41:43 donie-ThinkPad-T430 /etc/mysql/debian-start[37074]: There is no need to run mysql_upgrade again for >
Apr 25 16:41:43 donie-ThinkPad-T430 /etc/mysql/debian-start[37074]: You can use --force if you still want to run mys>
lines 14-20/20 (END)
"""



