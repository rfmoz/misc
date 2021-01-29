FROM debian:jessie

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    build-essential dh-systemd lintian git-buildpackage devscripts libpam0g-dev libldap2-dev libsasl2-dev libselinux1-dev autoconf bison flex libaudit-dev zlib1g-dev && \
    apt-get clean

WORKDIR /var/tmp/

RUN dget -u https://deb.debian.org/debian/pool/main/s/sudo/sudo_1.9.5p2-1.dsc && cd sudo-1.9.5p2/ && debian/rules binary


# Based on https://unix.stackexchange.com/questions/631438/update-sudo-in-debian-wheezy-for-cve-2021-3156
#
#	docker build -t "debian:jessie-sudo" .
#	docker run -v /tmp:/tmp/ --rm -ti debian:jessie-sudo bash -c 'cp /var/tmp/*deb /tmp/'
#	ls /tmp/*deb
