from time import gmtime, strftime, sleep
from threading import Thread
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class watcher(object):
    global txtTime
    global txtDate

    def repeat(self):
        while True:
            self.txtTime.set_text(strftime("%H:%M:%S", gmtime()))
            self.txtDate.set_text(strftime("%Y-%m-%d", gmtime()))
            sleep(1)

    def run(self,_txtTime,_txtDate):
        self.txtTime=_txtTime
        self.txtDate=_txtDate
        clock = Thread(target=self.repeat)
        clock.start()




