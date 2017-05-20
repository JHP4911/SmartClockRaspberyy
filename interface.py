import os
import gi

from notebook import notebook
from notes import notes

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from watcher import watcher
from systemTime import systemTime
from time import gmtime,strftime


class interface(object):
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("ekranlar.glade")
        self.main_window = self.builder.get_object("main")
        self.menu_window = self.builder.get_object("menu")
        self.date_window = self.builder.get_object("date")
        self.not_window = self.builder.get_object("notlar")
        self.lstNotes = self.builder.get_object("lstnot")
        self.program = self.builder.get_object("program")
        self.programDay = self.builder.get_object("programDay")

        renderer = Gtk.CellRendererText()
        colmn = Gtk.TreeViewColumn("Notlar", renderer, text=0)
        self.lstNotes.append_column(colmn)
        self.lstNotes.show_all()
        self.main_window.show()
        self.builder.connect_signals(self)
        self.setClockText()

    def setClockText(self):
        watcherText = watcher()
        _time = self.builder.get_object("saat")
        _date = self.builder.get_object("tarih")
        watcherText.run(_time, _date)

    def btnMenuOnClick(self, widget):
        self.main_window.hide()
        self.menu_window.show()

    def btnNotOnClick(self, widget):
        self.not_window.show()
        _model = Gtk.ListStore(str)
        _model.clear()
        readnotes = notes()
        noties = readnotes.read();
        for ndx, member in enumerate(noties):
            _model.append([member["not"]])
        self.lstNotes.set_model(_model)
        self.menu_window.hide()

    def btnAddNoteOnClick(self, widget):
        readnotes = notes()
        noties = readnotes.read();
        _txtNot = self.builder.get_object("txtnot")
        text = _txtNot.get_text()
        noties.append({"not": text})
        readnotes.write(noties)
        self.not_window.hide()
        self.menu_window.show()

    def btnDersOnClick(self, widget):
        self.menu_window.hide()
        self.program.show()

    def btnSaatOnClick(self, widget):
        self.menu_window.hide()
        self.date_window.show()
        self.builder.get_object("txtyil").set_text(strftime("%Y", gmtime()))  # Year
        self.builder.get_object("txtay").set_text(strftime("%m", gmtime()))  # Month
        self.builder.get_object("txtgun").set_text(strftime("%d", gmtime()))  # Day
        self.builder.get_object("txtsaat").set_text(strftime("%H", gmtime()))  # Hour
        self.builder.get_object("txtdakika").set_text(strftime("%M", gmtime()))  # Minute

    def btnHesapOnclick(self, widget):
        os.system("galculator")

    def btnGeriOnClick(self, widget):
        self.main_window.show()
        self.menu_window.hide()
        self.not_window.hide()
        self.date_window.hide()
        self.program.hide()
        self.programDay.hide()

    def btnDayOnClick(self, widget):
        self.program.hide()
        self.programDay.show()
        self.builder.get_object("label6").set_text(widget.get_label())
        notebook().readProgram(self.builder,widget.get_label())

    def btnGunKaydet(self, widget):
        gunLabel = self.builder.get_object("label6")
        notebook().writeProgram(self.builder,gunLabel.get_text())

    def btnSaatKaydetOnClick(self, widget):
        _setTime = systemTime()
        time_tuple = (
            self.builder.get_object("txtyil").get_text(),  # Year
            self.builder.get_object("txtay").get_text(),  # Month
            self.builder.get_object("txtgun").get_text(),  # Day
            self.builder.get_object("txtsaat").get_text(),  # Hour
            self.builder.get_object("txtdakika").get_text(),  # Minute
            0,  # Second
            0,  # Millisecond
        )
        _setTime.save(time_tuple)          
        self.main_window.show()
        self.menu_window.hide()
        self.date_window.hide()
