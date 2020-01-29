                       ---------------------------
                         wg-quick with DNSSearch
                       ---------------------------
                              29/Jan/2020



============
| Abstract |
============

This is a fork of the upstream "wg-quick" script located at: 

     https://git.zx2c4.com/wireguard-tools/

As modification, it only have implemented the option "DNSSearch", like is
already done with "DNS", who allows setting via resolvconf the "search"
field on resolv.conf

Available for Linux and FreeBSD.




===========
| Example |
===========

Add under '[Interface]' the term "DNSSearch =" with one or a comma separated
list of domain names:

    [Interface]
    ...
    DNSSearch = lan1.example.com, lan2.example.com




================
| Installation |
================

Two options:

1- Copy the file already patched
  
	Backup the original script and overwrite it with this new one:

		# mv /usr/bin/wg-quick /usr/bin/backup_wg-quick
		# cp ./linux.bash /usr/bin/wg-quick

2- Patch the original script
	
		# mv /usr/bin/wg-quick /usr/bin/backup_wg-quick
		# patch -p0 /usr/bin/wg-quick < linux.patch
