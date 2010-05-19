#!/usr/bin/env python

import wx

class clippyClipboard(wx.Clipboard):
    def __init__(self):
        wx.Clipboard.__init__(self)

    def updateWithText(self, text):
        txtObj = wx.TextDataObject()
        txtObj.SetText(text)

        if not self.IsOpened():
            self.Open()
            self.SetData(txtObj)
            self.Close()
