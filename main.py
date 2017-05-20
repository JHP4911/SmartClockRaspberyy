import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from interface import *

if __name__ == "__main__":
    intf = interface()
    Gtk.main()
