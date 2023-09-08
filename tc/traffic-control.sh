#!/bin/bash

# This scripts control incomming and outcomming bandwight in a linux router box
# The linux box only have one eth0 connect to the local network and other to internet
#  ifb0 is a a special device create only for limit the incomming bandwight in eth0
# It is configured for match a 192.168.1.0/24 network, with 255 hosts

# The limit for up/down is 20Mb (20480kbit), divide this bandwight for every host (in this case 80kbit)

# Interface connect to out lan
int1="eth0"
# Interface virtual for incomming traffic
tin1="ifb0"
# Lan address (without netmask part)
lan1="192.168.1."

# Create input forwarding device
ip link add dev $tin up type ifb


## Limit outcomming traffic (to internet)
# Clean interface
tc qdisc del root dev $int1
# Add classes per ip
tc qdisc add dev $int1 root handle 1: htb default 20
	tc class add dev $int1 parent 1: classid 1:1 htb rate 20480kbit
		for i in $(seq 1 255); do
			tc class add dev $int1 parent 1:1 classid 1:1$i htb rate 80kbit ceil 20480kbit
		done
# Match ip and put it into the respective class
for i in $(seq 1 255); do
	tc filter add dev $int1 protocol ip parent 1: prio 1 u32 match ip dst $lan1$i/32 flowid 1:1$i
done





## Limit incomming traffic ( to localhost)
# Clean interface
tc qdisc del dev $int1 handle ffff: ingress
tc qdisc del root dev $tin1
tc qdisc add dev $int1 handle ffff: ingress
# Redirecto ingress eth0 to egress ifb0
tc filter add dev $int1 parent ffff: protocol ip u32 match u32 0 0 action mirred egress redirect dev $tin1
# Add classes per ip
tc qdisc add dev $tin1 root handle 2: htb default 20
	tc class add dev $tin1 parent 2: classid 2:1 htb rate 20480kbit
		for i in $(seq 1 255); do
			tc class add dev $tin1 parent 2:1 classid 2:1$i htb rate 80kbit ceil 20480kbit 
		done

# Match ip and put it into the respective class
for i in $(seq 1 255); do
	tc filter add dev $tin1 protocol ip parent 2: prio 1 u32 match ip src $lan1$i/32 flowid 2:1$i
done
