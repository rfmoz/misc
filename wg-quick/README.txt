                       ---------------------------
                         wg-quick with DNSSearch
                       ---------------------------
                              11/May/2020


___

> **The functionality provided here was finally implemented on wireguard-tools v1.0.20200510**
>
> https://lists.zx2c4.com/pipermail/wireguard/2020-May/005415.html
>
>  * wg-quick: support dns search domains
>  
>  If DNS= has a non-IP in it, it is now treated as a search domain in
>  resolv.conf.  This new feature will be rolling out across our various GUI
>  clients in the next week or so.
>
>  DNS=8.8.8.8,8.8.4.4,mycorp.net
___



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
