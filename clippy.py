#!/usr/bin/env python

import wx

from TaskBarIcon import clippyTaskBarIcon
from MainWindow import clippyMainWindow

class clippy(wx.App):
    def OnInit(self):
        frame = clippyMainWindow(None, -1, 'clippy')
        frame.Show(False)
        self.SetTopWindow(frame)
        return True

app = clippy(0)
app.MainLoop()
