#!/usr/bin/env python

import signal, os, json, commands
from gi.repository import Gtk, GLib, AppIndicator3, Notify
from urllib2 import Request, urlopen, URLError

APPINDICATOR_ID = 'jokes'
INTERVAL = 1
signal.signal(signal.SIGINT, signal.SIG_DFL)

class MainClass:
	#def __init__(self):

	def update(self, arg):
		self.indicator.set_label(self.get_minifetch(), "")
		return True


	def fetch_joke(self):
		self.request = Request('http://api.icndb.com/jokes/random?limitTo=[nerdy]')
		self.response = urlopen(self.request)
		self.joke = json.loads(self.response.read())['value']['joke']
		return self.joke

	def joke(self, arg):
		Notify.Notification.new("<b>Random Joke:</b>", self.fetch_joke(), None).show()

	def test(self, arg):
		self.win = Gtk.Window()
		#win.connect("delete-event", gtk.main_quit)
		self.win.show_all()

	def build_menu(self):
		self.menu = Gtk.Menu()
		
		self.item_quit = Gtk.MenuItem('Quit')
		self.item_quit.connect('activate', self.quit)
		self.menu.append(self.item_quit)
		
		self.item_joke = Gtk.MenuItem('Joke')
		self.item_joke.connect('activate', self.joke)
		self.menu.append(self.item_joke)
		
		self.item_test = Gtk.MenuItem('Test')
		self.item_test.connect('activate', self.test)
		self.menu.append(self.item_test)

		self.menu.show_all()
		return self.menu

	def get_minifetch(self):
		self.kernel = commands.getoutput('date')
		return self.kernel
	
	def quit(self, arg):
		Notify.uninit()
		Gtk.main_quit()

	def main(self):
		self.indicator = AppIndicator3.Indicator.new(APPINDICATOR_ID, os.path.abspath('unnamed.png'), AppIndicator3.IndicatorCategory.SYSTEM_SERVICES)
		self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
		self.indicator.set_menu(self.build_menu())

		#self.indicator.set_label(self.get_minifetch(), "")
		#self.indicator.set_title(#function())

		self.update(self.indicator)
		GLib.timeout_add_seconds(INTERVAL, self.update, self.indicator)

		Notify.init(APPINDICATOR_ID)
		Gtk.main()

if __name__ == "__main__":
	widget = MainClass()
	widget.main()
