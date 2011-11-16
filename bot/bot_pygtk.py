#!/usr/bin/env python

"""
Handy functions for bots, based on PyGTK

by WangLu
"""

from gtk import gdk

import Xlib.display
import Xlib.X
import Xlib.XK
import Xlib.error
import Xlib.ext.xtest


def RGB(c):
    return (((c[0]<<8)+c[1])<<8)+c[2]

def take_screenshot(win = None):
    if win is None:
        win = gdk.get_default_root_window()
    sz = win.get_size()
    pb = gdk.Pixbuf(gdk.COLORSPACE_RGB, False, 8, sz[0], sz[1])
    pb = pb.get_from_drawable(win, win.get_colormap(), 0, 0, 0, 0, sz[0], sz[1])
    return pb.get_pixels_array()

def find_window(name, count):
    c = 0
    for w in Xlib.display.Display().screen().root.query_tree().children:
        cls = w.get_wm_class()
        if cls and cls[0] == name:
            c += 1
            if c == count:
                return w
    return None

win = None
gc = None
def draw_point(x,y):
    global win,gc
    if not win:
        win = find_window('draw', 1)
        print win
#        win = Xlib.display.Display().screen().root
        if win:
            gc = win.create_gc(foreground=0xff0000)
    if win:
        win.point(gc, x, y)


def move(x,y):
    display = Xlib.display.Display()
    Xlib.ext.xtest.fake_input(display, Xlib.X.MotionNotify, x=x, y=y)
    display.flush()

def click():
    mouse_down()
    mouse_up()

def mouse_down():
    display = Xlib.display.Display()
    Xlib.ext.xtest.fake_input(display, Xlib.X.ButtonPress, 1)
    display.sync()
def mouse_up():
    display = Xlib.display.Display()
    Xlib.ext.xtest.fake_input(display, Xlib.X.ButtonRelease, 1)
    display.sync()



