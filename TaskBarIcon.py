#!/usr/bin/env python

import wx

class clippyTaskBarIcon(wx.TaskBarIcon):
    def __init__(self, frame):
        wx.TaskBarIcon.__init__(self)

        self.frame = frame
        #self.SetIcon(wx.Icon('web.png', wx.BITMAP_TYPE_PNG), 'clippy.py')
        self.SetIcon(wx.Icon('clippy.png', wx.BITMAP_TYPE_PNG,  desiredWidth=16,  desiredHeight=16), 'clippy')
        self.Bind(wx.EVT_MENU, self.OnTaskBarActivate, id=1)
        self.Bind(wx.EVT_MENU, self.OnTaskBarDeactivate, id=2)
        self.Bind(wx.EVT_MENU, self.OnTaskBarClose, id=3)

        # Show the application's main window when clicking the taskbar icon
        wx.EVT_TASKBAR_LEFT_UP(self, self.OnTaskBarLeftUp)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        if not self.frame.IsShown():
            menu.Append(1, '&Show')
        else:
            menu.Append(2, '&Hide')
        menu.AppendSeparator()
        menu.Append(3, 'E&xit')
        return menu

    def OnTaskBarClose(self, event):
        #self.frame.Close()
        self.Destroy()
        self.frame.Destroy()

    def OnTaskBarActivate(self, event):
        if not self.frame.IsShown():
            self.frame.Show()

    def OnTaskBarDeactivate(self, event):
        if self.frame.IsShown():
            self.frame.Hide()

    def OnTaskBarLeftUp(self, event):
        if not self.frame.IsShown():
            self.frame.Show()
