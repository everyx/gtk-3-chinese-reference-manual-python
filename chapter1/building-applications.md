#构建应用程序

一个应用由许多文件构成：

* 可执行文件：对于 c/c++ 则是一个二进制文件，由于 Python 程序是解释执行的，所以实际上，对于 Python 程序则是指代码文件，并且都安装在 `/usr/bin` 下。
* 桌面文件：桌面文件为桌面 shell 提供了重要的程序描述信息。例如应用名，图标，D-Bus 名，命令行启动命令等。被安装在 `/usr/share/applications` 下。
* 图标：图标被安装在 `/usr/share/icons/hicolor/48x48/apps`，无论当前主题是什么，都能在这里找到。
* 设置 schema：如果一个程序使用 GSettings，他的 schema 将安装到 `/usr/share/glib-2.0/schemas`，这样像 dconf-editor 这类的工具就可以找到他了。
* 其他资源：对于使用 c/c++ 开发的 GTK+ 应用，其他文件，例如 GtkBuilder ui 文件，最好是从存储在应用自身二进制文件中的资源中加载。这就消除了通常被安装在 `/usr/share` 下的一个应用特定的位置的需要，但对于 Python 开发的 GTK+ 应用则仍需要使用常规的分离存储的方式。

GTK+ 包含建立在 [GApplication](https://developer.gnome.org/gio/unstable/GApplication.html) 上的应用支持。在这篇教程中，我们从无到有构建一个简单的应用，并逐渐一点点的增加功能。在这个过程中，我们将学习 GApplication，template, resources, application menu，setting，GtkHeaderBar，GtkStack，GtkSearchBar，GtkListBox 及更多知识。

完整的源文件可以在项目 github 仓库中的 code 目录下找到。

1. 一个小应用
2. 填充窗口
3. 打开文件
4. 一个应用菜单
5. 一个偏好对话框
6. 增加搜索栏
7. 增加侧边栏
8. 属性
9. 标题栏
