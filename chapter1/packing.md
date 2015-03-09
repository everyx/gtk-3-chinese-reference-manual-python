# 组装

创建一个程序时，你会想放不止一个控件到窗口中。我们的第一个 helloworld 例子只用了一个控件，所以我们简单的用 `Gtk.Container.add()` 来组装控件到窗口中。但是当你需要放多个控件到窗口中时，控制每个控件的位置和大小就变得重要了。这就是要用到组装的地方了。

GTK+ 自带了大量的布局容器，来控制添加到他们的子控件的布局。概览请阅 [布局容器](https://developer.gnome.org/gtk3/3.14/LayoutContainers.html)。

下面的例子显示了 GtkGrid 容器是如何让你排列多个按钮的：

![grid-packing.png](grid-packing.png)

**Example 2. Packing buttons**

新建一个名为 example-2.py 的文件。

```python
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
```

在终端输入以下命令用运行程序：

```shell
python3 example-2.py
```
