#!/usr/bin/env python3

from gi.repository import Gtk,GObject

class MyWindow(Gtk.Window):
    
    # 初始化一个窗体
    def __init__(self):
        
        # 使用默认初始化
        Gtk.Window.__init__(self)
        
        # 设置窗口标题
        self.set_title("hello world")
        
        # 设置边框宽度
        self.set_border_width(10)
        
        # 当这个窗体的发出 “delete-event” 信号（是由 GTK+ 响应从窗口管理器的事件时发出的，
        # 通常是点击 “关闭” 窗口控件的结果）的时候，我们让他调用下面定义的 on_delete_event 
        # 函数。
        self.connect("delete-event", self.on_delete_event)
        
        # 这里我们将 “destroy” 事件连接到 Gtk.main_quit 函数。当对这个窗体调用 
        # Gtk.Widget.destroy，或者当我们在 on_delete_event 回调时返回 False。
        self.connect("destroy", Gtk.main_quit)
        
        # 创建一个 label 为 “Hello World” 的新按钮。
        self.button = Gtk.Button.new_with_label("Hello World")
        
        # 当按钮接收到 "clicked" 信号时，将调用下面定义的 print_hello。
        self.button.connect("clicked", self.print_hello)
        
        # 注：原例中使用的时 g_signal_connect_swapped()，但是没有对应的 PyGObject 方法,
        # 所以这里变成了要自己写一个方法。
        self.button.connect("clicked", self.destroy_window)
        
        # 把按钮加入到窗口中，GtkWindow 继承自 GtkBin——一个只能有一个子元素的特殊容器。
        self.add(self.button)

    # 这是一个回调函数，下面几个也都是的。
    def print_hello(self, widget):
        print("Hello World\n")

    def on_delete_event(self, widget, event):
        # 如果在 "delete-event" 信号处理函数中返回 False，GTK 将发出 "destroy" 信号。
        # 返回 True 意味着你不想窗口被销毁。
        # 
        # 这个用来处理弹出“你确定想要推出吗？”这种情况最有用了。
        print("delete event occurred\n")
        return True

    def destroy_window(self, widget):
        Gtk.Widget.destroy(self)

# 创建一个窗体对象
window = MyWindow()

# 显示窗体的所有控件
window.show_all()

# 所有的程序必须有一个 Gtk.main()。程序控制到这里就结束了，下面就等待这事件的发生（比如一个按
# 钮按下或者一个鼠标事件），直到 Gtk.main_quit() 被调用。
Gtk.main()
