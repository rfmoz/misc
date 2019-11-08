check_conn1.patch
	Add to freebsd-install a function to check the internet connectivity before the process of getting files from internet.
	It avoids a hard exit in the middle of the freebsd-install process if the network is bad.
	Tested in 12.0 and 12.1

	Apply with:
            cp /usr/sbin/freebsd-update /tmp/freebsd-update.bkp
            patch /usr/sbin/freebsd-update < check_conn1.patch
