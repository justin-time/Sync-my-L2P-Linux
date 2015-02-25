INSTALL_FILE := install -m644 -D
INSTALL_PROGRAM := install -m755 -D
INSTALL_DIR := install -m755 -d

CP := cp -rf
RM := rm -f
LN := ln -s
GZIP := gzip -f9
QMAKE := qmake
MAKE := make

ICON_SIZES = 16 32 48 128

MAKEFILE = syncmyl2p.mk
exec_prefix = $(prefix)
bindir = $(prefix)/bin
dataroot = $(prefix)/share


all:
	$(QMAKE) -o $(MAKEFILE)
	$(MAKE) -f $(MAKEFILE)

install:
	$(INSTALL_DIR) $(DESTDIR)$(bindir)
	$(INSTALL_DIR) $(DESTDIR)$(dataroot)/applications
	$(INSTALL_DIR) $(DESTDIR)$(dataroot)/icons
	$(INSTALL_PROGRAM) Sync-my-L2P           $(DESTDIR)$(bindir)
	$(INSTALL_FILE) linux/Sync-my-L2P.desktop $(DESTDIR)$(dataroot)/applications
	$(CP) linux/hicolor    $(DESTDIR)$(dataroot)/icons

uninstall:
	$(RM) $(DESTDIR)$(bindir)/Sync-My-L2P
	$(RM) $(DESTDIR)$(dataroot)/applications/Sync-my-L2P.desktop
	$(foreach SIZE,$(ICON_SIZES),$(RM) $(DESTDIR)$(dataroot)/icons/hicolor/$(SIZE)x$(SIZE)/apps/sync-my-L2P.png ;)


clean:
	[ ! -f $(MAKEFILE) ] || $(MAKE) -f $(MAKEFILE) clean

distclean: clean
	[ ! -f $(MAKEFILE) ] || $(MAKE) -f $(MAKEFILE) distclean

