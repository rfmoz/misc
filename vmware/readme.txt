# Installation vmware-view-client in Debian 8 Jessie


dpkg --add-architecture i386
apt-get update
apt-get install gdebi
gdebi libssl0.9.8_0.9.8o-7ubuntu3.1_i386.deb 
gdebi vmware-view-client_2.2.0-0ubuntu0.12.04_i386.deb 
