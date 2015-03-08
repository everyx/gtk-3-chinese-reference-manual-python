# 基础

我们用一个最简单的程序来开始对GTK的介绍，下面的程序将创造一个200×200像素的窗体。

![Window](window_default.png)

新建一个名为 `example-0.py` 的文件，写入如下内容：

```python
#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.set_title("Window")
window.connect("destroy", Gtk.main_quit)
window.show()
Gtk.main()
```

然后在终端输入以下命令运行程序：
```shell
python3 example-0.py
```
所有使用 Python 编写的 GTK+ 程序都必须从 `gi.repository` 包导入 Gtk 模块，这样
我们才能愉快的访问 GTK+ 类和方法。

接下来我们通过 `Gtk.Window()` 创建了一个空窗口。默认这个窗体的类型是 `GTK_WINDOW_TOPLEVEL`，
也就是说这个 GtkWindow 将会被系统的窗口管理器管理：由一窗口，一个标题栏和窗口控
件组成，系统不同显示效果也不尽相同。

为了在 `GtkWindow` 销毁时正确终止程序，我们连接"`destroy`" 信号给 Gtk.main_quit() 
函数。这个函数将终止由下面 `Gtk.main()` 启动的 GTK+ 主循环。"`destory`" 信号会
窗口控件销毁时发出，也会在显示调用 `Gtk.Widget.destroy()`或者失去父级控件时发出。
顶层 `GtkWindows` 也会在点击窗口关闭控制按钮时发出。

GtkWidgets 默认时隐藏的，通过在一个控件上调用 `show()`，告诉 GTK+ 设置 visibility 
属性来让控件可见。这一切都会在主循环启动后完成。

最后以行调用了 `Gtk.main()`。这个函数会启动 GTK+ 主循环并阻塞程序的控制流直到 
`Gtk.main_quit()` 函数被调用。

程序运行时，GTK+ 接收事件，典型的事件是用户通过程序界面进行的一些输入事件，也
可以是窗口管理器或者其他程序的消息。GTK+ 处理这些事件，作为结果也就是信号也许就
从你的控件中发出。通常你想要你的程序响应用户的输入，你就要将这些信号连接到对应
的处理器。

下面这个例子略有些复杂，试着展示了一些 GTK+ 的能力。

按照编程传统，我们叫他 *Hello, World*。

![hello-world.png](hello-world.png)

**Example 1. Hello World in GTK+**

新建一个如下内容且名为 example-1.py 的文件：

```python
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
```

然后在中终端中输入命令运行：

```shell
python3 example-1.py
```

