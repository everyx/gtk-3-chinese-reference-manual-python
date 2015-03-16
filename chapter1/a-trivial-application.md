# 一个小应用

当使用 GtkApplication，主函数将非常简单。我们只需要调用 `Gtk.Application.run()` 就行了。

```python
from gi.repository import Gtk

class MyWindow(Gtk.ApplicationWindow):
   def __init__(self, app):
      Gtk.Window.__init__(self, application=app)

class MyApplication(Gtk.Application):
   def __init__(self):
      Gtk.Application.__init__(self);

   def do_activate(self):
      win = MyWindow(self)
      win.present()

   def do_open(self, file, hint):
      win = self.get_window()
      
      if win Null:
         win = MyWindow(self)
      
      for i in 

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
```

所有的程序逻辑都在Gtk.Application 的子类 MyApplication 类中。我们的例子暂时还没有什么好玩的功能，所做的仅仅是在无餐激活时打开一个窗口，而在有参数时打开这个给定的文件。

要处理这两种情况，我们重载了 `do_activate()` 虚函数，也就是那个在没有命令行参数的情况下程序启动时调用的方法，`do_open()` 虚函数则是在程序以命令行参数方式启动时调用的。

要学习更多的 GApplication 知识，清查阅 GIO 文档。
