#!/usr/bin/env python

import signal
import os
import json
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify
from urllib2 import Request, urlopen, URLError

APPINDICATOR_ID = 'jokes'

signal.signal(signal.SIGINT, signal.SIG_DFL)

def fetch_joke():
	request = Request('http://api.icndb.com/jokes/random?limitTo=[nerdy]')
	response = urlopen(request)
	joke = json.loads(response.read())['value']['joke']
	return joke

def joke(_):
	notify.Notification.new("<b>Random Joke:</b>", fetch_joke(), None).show()

def test(_):
	win = gtk.Window()
	#win.connect("delete-event", gtk.main_quit)
	win.show_all()

def build_menu():
	menu = gtk.Menu()
	
	item_quit = gtk.MenuItem('Quit')
	item_quit.connect('activate', quit)
	menu.append(item_quit)
	
	item_joke = gtk.MenuItem('Joke')
	item_joke.connect('activate', joke)
	menu.append(item_joke)
	
	item_test = gtk.MenuItem('Test')
	item_test.connect('activate', test)
	menu.append(item_test)

	menu.show_all()
	return menu
 
def quit(_):
	notify.uninit()
	gtk.main_quit()

def main():
	indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('unnamed.png'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
	indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
	indicator.set_menu(build_menu())

	notify.init(APPINDICATOR_ID)
	gtk.main()

main()
