FROM debian:wheezy

ENV DEBIAN_FRONTEND noninteractive

RUN echo "deb http://archive.debian.org/debian/ wheezy contrib main non-free" > /etc/apt/sources.list && \
    echo "deb-src http://archive.debian.org/debian/ wheezy contrib main non-free" >> /etc/apt/sources.list && \
    apt-get update && apt-get install -y apt-utils && \
    apt-get install -y --force-yes \
    curl gcc make sudo wget expect gnupg perl-base=5.14.2-21+deb7u3 perl \
    libc-bin=2.13-38+deb7u10 libc6=2.13-38+deb7u10 libc6-dev build-essential \
    cdbs devscripts equivs automake autoconf libtool libaudit-dev \
    libdb5.1=5.1.29-5 libdb5.1-dev libssl1.0.0=1.0.1e-2+deb7u20 procps gawk libsigsegv2 \
    libpam0g-dev libldap2-dev libsasl2-dev libselinux1-dev bison flex zlib1g-dev

WORKDIR /var/tmp/

RUN dget -u https://deb.debian.org/debian/pool/main/s/sudo/sudo_1.9.5p2-1.dsc && cd sudo-1.9.5p2/ && debian/rules binary


# Based on https://unix.stackexchange.com/questions/631438/update-sudo-in-debian-wheezy-for-cve-2021-3156
#
#	docker build -t "debian:wheezy-sudo"
#	docker run -v /tmp/:/tmp/ --rm -ti debian:wheezy-sudo bash -c 'cp /var/tmp/*deb /tmp'
#	ls /tmp/*deb
