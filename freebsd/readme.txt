check_conn1.patch
	Add to freebsd-install a function to check the internet connectivity before the process of getting files from internet.
	It avoids a hard exit in the middle of the freebsd-install process if the network is bad.
	Tested from 12.0 to 14.1

	Apply with:
            cp /usr/sbin/freebsd-update /var/tmp/freebsd-update.bkp
            patch /usr/sbin/freebsd-update < check_conn1.patch


add_fast1.patch
	Add "--fast" argument option to freebsd-update. It tries to skip cpu intensive tasks, skipping sha256 checks when possible and set gzip calls with the lowest compression level.
	Tested from 12.0 14.1

	Apply with:
            cp /usr/sbin/freebsd-update /var/tmp/freebsd-update.bkp
            patch /usr/sbin/freebsd-update < add_fast1.patch


