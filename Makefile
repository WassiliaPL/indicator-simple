all:
	@echo "Type 'make install' (root) to install"
	@echo "Type 'make uninstall' (root) to uninstall"

install:
	install indicator-simple $(DESTDIR)/usr/bin

uninstall:
	rm -f $(DESTDIR)/usr/bin/indicator-simple

.PHONY: install uninstall
