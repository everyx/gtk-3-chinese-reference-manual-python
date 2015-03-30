# 一个应用菜单

应用菜单是有 GNOME shell 显示在屏幕上端的，意思就是一些影响整个应用的常用动作都要放在这里。

和窗体模板一样，我们在一个 UI 文件中指定应用菜单，并且将他编译成资源文件。

```xml
<?xml version="1.0"?>
<interface>
  <!-- interface-requires gtk+ 3.0 -->
  <menu id="appmenu">
    <section>
      <item>
        <attribute name="label" translatable="yes">_Preferences</attribute>
        <attribute name="action">app.preferences</attribute>
      </item>
    </section>
    <section>
      <item>
        <attribute name="label" translatable="yes">_Quit</attribute>
        <attribute name="action">app.quit</attribute>
      </item>
    </section>
  </menu>
</interface>
```

为了将应用程序和菜单关联起来，我们需要调用 `Gtk.Application.set_app_menu()` 。当激活的 
GActions 让应用菜单正式工作时，我们也要加如适当的动作到我们的程序中。

所有这些任务最好在 `do_startup()` 中完成，保证在每个应用程序实例中只被调用一次。

```python
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
```

我们的 preferences 菜单现在还啥都不能做，但是 Quit 菜单是一个功能完整。注意，快捷键 `Ctrl-Q` 
也可以激活 Quit。这是在通过 `Gtk.Application.set_accels_for_action()` 添加的。

应用菜单时这样的：

![getting-started-app4.png](../code/chapter1/application4/getting-started-app4.png)
