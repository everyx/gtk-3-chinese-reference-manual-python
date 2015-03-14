#!/usr/bin/env python3

from gi.repository import Gtk

def print_hello(widget, data=None):
    print("Hello World")

def main():
    builder = Gtk.Builder()
    builder.add_from_file("builder.ui")
    
    window = builder.get_object("window")
    window.connect("destroy", Gtk.main_quit)

    button = builder.get_object("button1")
    button.connect("clicked", print_hello)

    button = builder.get_object("button2")
    button.connect("clicked", print_hello)

    button = builder.get_object("quit")
    button.connect("clicked", Gtk.main_quit)

    Gtk.main()

if __name__ == '__main__':
    main()
