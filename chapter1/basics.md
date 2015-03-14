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
{% include "../code/chapter1/example-1.py" %}
```

然后在中终端中输入命令运行：

```shell
python3 example-1.py
```

