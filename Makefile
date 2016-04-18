all:
	@echo "Type 'make install' (root) to install"
	@echo "Type 'make uninstall' (root) to uninstall"

install:
	install indicator-simple /usr/bin
	install indicator-simple.desktop /usr/share/applications

uninstall:
	rm -f /usr/bin/indicator-simple
	rm -f /usr/share/applications/indicator-simple.desktop

.PHONY: install uninstall
