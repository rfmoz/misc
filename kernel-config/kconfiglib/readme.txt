## Kconfiglib process to get the kernel configuration as a tree list.


- Clone the repo inside the linux source dir:

/usr/src/linux-source-4.9# git clone git://github.com/ulfalizer/Kconfiglib.git

- Patch it:

patch -p1 < Kconfiglib/makefile.patch

- Configure as needed:

make menuconfig

- Get the menu as a tree list:

make scriptconfig SCRIPT=Kconfiglib/examples/print_config_tree.py SCRIPT_ARG=.config
