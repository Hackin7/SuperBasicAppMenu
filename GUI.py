import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository.GdkPixbuf import Pixbuf
from main import *
import os
appList = appListGenerate()
class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="SuperBasicAppLauncher")
        self.set_default_size(1000, 1000)
        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        #self.add(self.button)
        
        sw = Gtk.ScrolledWindow()
        self.liststore = Gtk.ListStore(Pixbuf, str, str, str)
        iconview = Gtk.IconView.new()
        iconview.set_model(self.liststore)
        iconview.set_pixbuf_column(0)
        iconview.set_text_column(1)
        for name, comment, icon, cmd in appList:
            print(icon)
            try:
                pixbuf = Gtk.IconTheme.get_default().load_icon(icon, 64, 0)
                self.liststore.append([pixbuf, name, comment, cmd])
            except: pass
        iconview.connect('item-activated', self.item_activated)
        iconview.grab_focus()
        sw.add_with_viewport(iconview)
        self.add(sw)
    def item_activated(self, iconview, tree_path):
        item = self.liststore[tree_path][3]
        print(item)
        os.system(item)
        #print(iconview, tree_path, item)

    def on_button_clicked(self, widget):
        print("Hello World")

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
