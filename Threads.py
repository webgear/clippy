#!/usr/bin/env python

import wx

from threading import Thread

class clippyClipboardThread(Thread):
    def __init__(self, mainWindow, clipboardHandle, dbHandle):
        # Start a new thread that will continually check the clipboard for changes
        Thread.__init__(self)

        self.clipboard = clipboardHandle
        self.db = dbHandle
        self.mainWindow = mainWindow

    def run(self):
        print "[MAIN THREAD] up and running..."

    def updateClipboard(self, event):
        if not self.clipboard.IsOpened():
            self.clipboard.Open()
            success = self.clipboard.IsSupported(wx.DataFormat(wx.DF_TEXT))
            clipText = wx.TextDataObject()
            clipData = self.clipboard.GetData(clipText)
            self.clipboard.Close()

            if success:
                clipboardText = clipText.GetText()

                if clipboardText != '' and clipboardText is not None:
                    # check the db
                    status = self.db.ClipExists(clipboardText)

                    if status[0] == 0:
                        # create new snippet
                        self.db.CreateClip(clipboardText)
