# Sync-my-L2P-Linux
This repository contains all files to build Sync-my-L2P on linux.

### Building native DEB/RPM packages

The folder "DEB support" contains all files to create native Debain-Packages for Debain/Ubuntu/Linux Mint. 
The other folder "RPM support" contains the spec-file and the changelog to build Sync-my-L2P for Fedora and openSUSE.

Attention! Please notice that you need a valid CliendID to connect to the RWTH servers!

### Building from source code
 1. Make sure that you have installed the following dependences: 
  * Ubuntu/Debian: qt5-qmake (>= 5.2) , libssl-dev, qt5-default (>= 5.2)
  * openSUSE: libopenssl-devel libqt5-qtbase-devel (>= 5.2) libudev-mini1 libqt5-qttools-devel (>= 5.2)
  * Fedora: openssl-devel qt5-qtbase-devel (>= 5.2)
 2. Download the source code from https://github.com/Sync-my-L2P/Sync-my-L2P
 3. Add a valid CliendID into the clientId.h file
 4. Copy the Makefile into the source code
  * Ubuntu/Debian: use the Makefile of the "DEB support" folder
  * openSUSE/Fedora: use the Makefile of the "RPM support" folder
 5. Open a terminal and go into the directory which contains the source code and enter: ``$ make`` to build the program.
 6. Now you can start Sync-my-L2P by opening the file `Sync-my-L2P`
 7. <i>OPTIONAL:</i> If you want to install the program system-wide enter as root: ``# make install DESTDIR=/usr``  <br />
    To deinstall the Programm, enter as root: ``# make uninstall``
