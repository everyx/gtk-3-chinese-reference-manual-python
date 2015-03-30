#!/usr/bin/env python3

import sys
import os
import signal
from gi.repository import Gtk, Gio, GObject
                 
class ExampleAppWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, application=app)
        self.set_template_from_resource('/org/gtk/exampleapp/window.ui')
        self.init_template()
        
        self.stack = self.get_object_by_name(self, 'stack')
      
    def get_object_by_name(self, widget, name):
        if isinstance(widget, Gtk.Container) is not True:
            return None
        else:
            lists = widget.get_children()
            for list in lists:
                list_name = Gtk.Buildable.get_name(list)
                if list_name == name:
                    return list
                else:
                    result = self.get_object_by_name(list, name)
                    if result is not None:
                        return result

class ExampleApp(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self,
                               application_id='org.gtk.exampleapp',
                               flags=Gio.ApplicationFlags.HANDLES_OPEN);

    def do_activate(self):
        self.win = ExampleAppWindow(self)
        self.win.present()

    def do_open(self, files, n_files, hint):
        windows = self.get_windows()
      
        if hasattr(self, 'win') and self.win is not None:
            self.win = windows.data()
        else:
            self.win = ExampleAppWindow(self)
         
        for file in files:
            example_app_window_open(self.win, file)
      
        self.win.present()
        
    def do_startup(self):
        Gtk.Application.do_startup(self)
                
        # can not use add_action_enteirs, see https://bugzilla.gnome.org/show_bug.cgi?id=678655
        preferencesAction = Gio.SimpleAction.new('preferences', None)
        preferencesAction.connect('activate', self.preferences_activated)
        self.add_action(preferencesAction)
        
        quitAction = Gio.SimpleAction.new('quit', None)
        quitAction.connect('activate', self.quit_activated)
        self.add_action(quitAction)
        
        self.set_accels_for_action('app.quit', ['<Ctrl>Q'])
        
        builder = Gtk.Builder()
        builder.add_from_resource('/org/gtk/exampleapp/app-menu.ui')
        
        appMenu = builder.get_object('appmenu')
        self.set_app_menu(appMenu)

    def preferences_activated(self, action, param=None):
        pass

    def quit_activated(self, action, param=None):
        self.quit()
        pass

def example_app_window_open(win, file):
    basename = file.get_basename()
    
    scrolled = Gtk.ScrolledWindow()
    scrolled.set_hexpand(True)
    scrolled.set_vexpand(True)
    scrolled.show()
        
    view = Gtk.TextView()
    view.set_editable(False)
    view.set_cursor_visible(False)
    view.show()
    
    scrolled.add(view)
    win.stack.add_titled(scrolled, basename, basename)
    
    result = file.load_contents()
    isLoaded = result[0]
    contents = result[1].decode('utf-8')
    if isLoaded:
        buffer = view.get_buffer()
        buffer.set_text(contents)
        
    del(file)
    
if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    
    resource = Gio.resource_load("exampleapp.gresource")
    Gio.Resource._register(resource)

    app = ExampleApp()
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)
