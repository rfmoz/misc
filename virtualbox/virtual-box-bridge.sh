#!/bin/sh

WAN_INET='wlp2s0'  # Define here wan interface (Usually wifi or wired from host)
USER_VBOX='user1'  # User for run the Virtualbox guest
VBGUEST1='VirtualBoxGuest1'  # Name of virtual guest 1
VBGUEST2='VirtualBoxGuest2'  # Name of virtual guest 2
VBGUEST3='VirtualBoxGuest3'  # Name of virtual guest 3
PATH=/sbin:/usr/bin:/bin:/usr/bin:/usr/sbin


# Create tap interfaces
ip tuntap add name tap0 mode tap
ip link set up dev tap0
ip tuntap add name tap1 mode tap
ip link set up dev tap1
ip tuntap add name tap2 mode tap
ip link set up dev tap2

# Create the bridge and add interfaces
ip link add name br0 type bridge
ip link set tap0 master br0
ip link set tap1 master br0
ip link set tap2 master br0		

# Set the IP address to bridge and routing
ip link set up dev br0
ip addr add 192.168.0.1/24 dev br0
ip route add 192.168.0.0/24 dev br0

# Allow ip forward
echo 1 > /proc/sys/net/ipv4/ip_forward

# NAT outbound traffic
iptables -t nat -A POSTROUTING -o ${WAN_INET} -j MASQUERADE

# Enable when docker is running too
iptables -A FORWARD -o br0 -j ACCEPT
iptables -A FORWARD -i br0 -j ACCEPT



## In the virtuabox guest (Example for 1st guest):

# Configure with a "Bridge interface" and choose between "tap0", "tap1" or "tap2".

# Set a fixed ip address. For Debian "/etc/network/interfaces":
#
# auto enp0s3
# iface enp0s3 inet static
# address 192.168.0.2
# netmask 255.255.255.0
# gateway 192.168.0.1

read -p "${VBGUEST1}? " -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]
then
        su - ${USER_VBOX} -c "vboxmanage startvm ${VBGUEST1}"
fi
echo ''

# Now it is possible to access trought network from the host (br0: 192.168.0.1) to the guest (192.168.0.2) and from the guest to the host and internet.
