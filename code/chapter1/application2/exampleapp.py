#!/usr/bin/env python

import sys
import os
from gi.repository import Gtk, Gio

class ExampleAppWindow(Gtk.ApplicationWindow):
   def __init__(self, app):
      Gtk.Window.__init__(self, application=app)
      self.set_template_from_resource('/org/gtk/exampleapp/window.ui')
      self.init_template()

class ExampleApp(Gtk.Application):
   def __init__(self):
      Gtk.Application.__init__(self,
                               application_id='org.gtk.exampleapp',
                               flags=Gio.ApplicationFlags.HANDLES_OPEN);

   def do_activate(self):
      win = ExampleAppWindow(self)
      win.present()

   def do_open(self, files, hint):
      windows = self.get_windows()
      
      if win is not None:
         win = windows.data()
      else:
         win = ExampleAppWindow(self)
         
      for file in files:
        example_app_window_open(win, file)
      
      win.present()

def example_app_window_open(win, file):
    pass
    
if __name__ == "__main__":
    resource = Gio.resource_load("exampleapp.gresource")
    Gio.Resource._register(resource)

    app = ExampleApp()
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)
