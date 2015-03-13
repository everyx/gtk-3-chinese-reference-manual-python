# 构建用户界面

当构建一个更加复杂的用户界面，拥有几十上百的控件时，使用 C 代码来处理所有的设置工作时非常麻烦的，而且让后期更改变得几乎不可能。

谢天谢地，通过使用一种可以通过 GtkBuilder 类解析的 xml 格式的 UI 描述文件，GTK+ 支持这些业务逻辑和用户界面的布局分离。

**Example 4. Packing buttons with GtkBuilder**

创建一个包含以下内容且名为 example-4.py 的文件。

```python
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
```

创建一个包含以下内容且名为 builder.ui 的文件。

```xml
<interface>
  <object id="window" class="GtkWindow">
    <property name="visible">True</property>
    <property name="title">Grid</property>
    <property name="border-width">10</property>
    <child>
      <object id="grid" class="GtkGrid">
        <property name="visible">True</property>
        <child>
          <object id="button1" class="GtkButton">
            <property name="visible">True</property>
            <property name="label">Button 1</property>
          </object>
          <packing>
            <property name="left-attach">0</property>
            <property name="top-attach">0</property>
          </packing>
        </child>
        <child>
          <object id="button2" class="GtkButton">
            <property name="visible">True</property>
            <property name="label">Button 2</property>
          </object>
          <packing>
            <property name="left-attach">1</property>
            <property name="top-attach">0</property>
          </packing>
        </child>
        <child>
          <object id="quit" class="GtkButton">
            <property name="visible">True</property>
            <property name="label">Quit</property>
          </object>
          <packing>
            <property name="left-attach">0</property>
            <property name="top-attach">1</property>
            <property name="width">2</property>
          </packing>
        </child>
      </object>
      <packing>
      </packing>
    </child>
  </object>
</interface>
```

通过一下命令运行程序：

```shell
python3 example-4.py
```

注意 GtkBuilder 也可以被用来构建非控件对象，例如树状结构，调节器等。这就是我们在这里使用 `gtk_builder_get_object()` 方法并返回一 GObject 而不是 GtkWidget。

通常，我们需要使用一个完成的路径给 `gtk_builder_get_object()` 来让程序不依赖当前路径运行。UI 描述文件放置位置常位于 /usr/share/appname。

另外，也可以将 UI 描述用一个字符串放在源代码中，并使用 `gtk_builder_add_from_string()` 来加载，但将 UI 描述单独用文件保存由几个好处：后面的 UI 调整不需要重新编译程序就可完成，并且更重要的是，可是花 UI 编辑器，例如 glade，可以加载文件并通过点击修改来创建和修改 UI。
