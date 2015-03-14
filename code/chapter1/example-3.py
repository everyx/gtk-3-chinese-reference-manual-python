#!/usr/bin/env python3

from gi.repository import Gtk, Gdk
import cairo

# 用来存储当前涂鸦的表面
surface = None

def clear_surface():
    global surface

    cr = cairo.Context(surface)
    
    cr.set_source_rgb(1, 1, 1)
    cr.paint()

    del cr

# 创建一个大小合适的新表面来存储涂鸦
def configure_event_cb(wid ,evt):
    global surface

    if surface is not None:
        del surface
        surface = None

    win = wid.get_window()

    surface = win.create_similar_surface(
        cairo.CONTENT_COLOR,
        wid.get_allocated_width(),
        wid.get_allocated_height())

    # 初始化绘制表面为空白
    clear_surface()
    
    # 我们已经处理配置了事件，不需要进行下一步的处理
    return True


# 重绘绘制表面。注意 draw 接收一个现成的已被剪切到只有控件需要绘制的部分的 cairo。
def draw_cb(wid, cr):
    global surface

    cr.set_source_surface(surface,0,0)
    cr.paint()
    return False

# 在给定的位置绘制一个矩形
def draw_brush(wid,x,y):
    global surface
    
    # 绘制到我们用来存储状态的 surface 上
    cr = cairo.Context(surface)
    cr.set_source_rgb(0,0,0)
    cr.rectangle(x-3,y-3,6,6)
    cr.fill()
    del cr
    
    # 现在受影响的绘制区域无效。
    wid.queue_draw_area(x-3,y-3,6,6)

# 无论是要绘制一个矩形或者清除这个 surface，处理按钮按下事件，取决于那个按钮被按下。
# button-press 信号处理器接收一个包含这些信息的 GdkEventButton 结构体。
def button_press_event_cb(wid, evt):
    global surface

    # 进行 paranoia 检查，例如在我们没有得到一个配置好的事件情况下
    if surface is None:
        return False

    if evt.button == Gdk.BUTTON_PRIMARY:
        draw_brush(wid,evt.x,evt.y)
    elif evt.button == Gdk.BUTTON_SECONDARY:
        clear_surface()
        wid.queue_draw()

    # 我们已经处理了这个事件，停止处理
    return True


# 处理移动事件，如果按钮 1 一直被按下，则持续的进行绘制。motion-notify 
# 信号处理器接收一个包含这些信息的 GdkEventMotion 结构体
def motion_notify_event_cb(wid,evt):
    global surface
    
    # 进行 paranoia 检查，例如在我们没有得到一个配置好的事件情况下
    if surface is None:
        return False

    if evt.state & Gdk.EventMask.BUTTON_PRESS_MASK:
        draw_brush(wid,evt.x,evt.y)

    # 我们已经处理了这个事件，停止处理
    return True


def close_window(wid):
    global surface

    if surface is not None:
        del surface
        surface = None

    Gtk.main_quit()


if __name__ == '__main__':
    win = Gtk.Window()
    win.set_title('Drawing Area')
    win.connect('destroy',close_window)
    win.set_border_width(8)

    frame = Gtk.Frame()
    frame.set_shadow_type(Gtk.ShadowType.IN)
    win.add(frame)

    da = Gtk.DrawingArea()
    # 设置一个最小大小
    da.set_size_request(100,100)
    frame.add(da)

    # 用于处理后段 surface 的信号
    da.connect('draw',draw_cb)
    da.connect('configure-event',configure_event_cb)

    # 事件信号
    da.connect('motion-notify-event',motion_notify_event_cb)
    da.connect('button-press-event',button_press_event_cb)
    
    # 请求接收事件，绘图区域通常不会订阅这些事件。特别是我们想要请求处理的的是
    # 按钮按下和移动通知事件。
    da.set_events(da.get_events() | Gdk.EventMask.BUTTON_PRESS_MASK | Gdk.EventMask.POINTER_MOTION_MASK)

    win.show_all()
    Gtk.main()
