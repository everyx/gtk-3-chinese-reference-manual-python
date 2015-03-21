# 一个小应用

当使用 GtkApplication，主函数将非常简单。我们只需要调用 `Gtk.Application.run()` 就行了。

```python
#!/usr/bin/env python

import sys
from gi.repository import Gtk, Gio
    
if __name__ == "__main__":
    app = ExampleApp()
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)
```

所有的程序逻辑都在 Gtk.Application 的子类 MyApplication 类中。我们的例子暂时还没有什么好玩的功能，所做的仅仅是在无餐激活时打开一个窗口，而在有参数时打开这个给定的文件。

要处理这两种情况，我们重载了 `do_activate()` 虚函数，也就是那个在没有命令行参数的情况下程序启动时调用的方法，`do_open()` 虚函数则是在程序以命令行参数方式启动时调用的。

要学习更多的 GApplication 知识，清查阅 GIO 文档。

```python
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
```

另外一个作为 GTK+ 应用支持的重要的类是 GtkApplicationWindow。通常都是用他的子类。我们的窗口啥都没干，所以窗口空空如也。

```python
class ExampleAppWindow(Gtk.ApplicationWindow):
   def __init__(self, app):
      Gtk.Window.__init__(self, application=app)
```

> [查看完整的代码](../code/chapter1/application1/exampleapp.py)

作为初始化步骤的一部分，我们也要创建一个应用图标和桌面文件。

![exampleapp.png](../code/chapter1/application1/exampleapp.png)

```ini
[Desktop Entry]
Type=Application
Name=Example
Icon=exampleapp
StartupNotify=true
Exec=@bindir@/exampleapp
```

注意这个 `@bindir@` 需要在这个桌面文件被使用前需要替换为实际路径。

这就是我们目前为止实现的：

![getting-started-app1.png](../code/chapter1/application1/getting-started-app1.png)

目前看起来还不是那么令人印象深刻，但是程序已经展现在会话总线上，他有着单实例语义，并且接收文件作为命令行参数。
