#!/usr/bin/env python3

from gi.repository import Gtk,GObject

def print_hello(self, widget):
    print("Hello World")
        
class MyWindow(Gtk.Window):
    
    def __init__(self):
        # 初始化窗体并设置标题
        Gtk.Window.__init__(self)
        self.set_title("Grid")
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(10)
        
        # 这里构造用来放置按钮的容器
        grid = Gtk.Grid()
        self.add(grid)
        
        button = Gtk.Button.new_with_label("Button 1")
        button.connect("clicked", print_hello, None)
        
        # 在网格单元 (0, 0) 放置第一个按钮，并让他刚好填满垂直
        # 和水平方向上的 1 个单元（也就是说没有跨行）。
        # 译者注：在大多数的图形界面库中坐标系都是以屏幕左上角为
        # 原点，向下为 y 轴正方向，向右为 x 轴正方向。
        grid.attach(button, 0, 0, 1, 1)
        
        button = Gtk.Button.new_with_label("Button 2")
        button.connect("clicked", print_hello, None)
        
        # 将第二个按钮放在网格单元 (1, 0)，并让他刚好填满垂直
        # 和水平方向上的 1 个单元（也就是说没有跨行）
        grid.attach(button, 1, 0, 1, 1)
        
        button = Gtk.Button.new_with_label("Quit")
        button.connect("clicked", Gtk.main_quit)
        
        # 将 Quit 按钮放在网格单元 (0, 1)，并让他跨越两列。
        grid.attach(button, 0, 1, 2, 1)

window = MyWindow()
window.show_all()
Gtk.main()
