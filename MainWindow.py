#!/usr/bin/env python

import wx

from DB import clippyDB

from TaskBarIcon import clippyTaskBarIcon

from Clipboard import clippyClipboard

from Threads import clippyClipboardThread

from TreeControls import clippyMainSnippetsTree

class clippyMainWindow(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, (-1, -1), (600, 500))
        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        self.tskic = clippyTaskBarIcon(self)
        self.Centre()
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        # Build and hook main menu to the application
        filemenu= wx.Menu()
        helpmenu = wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        fileMenuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Exit application")
        self.Bind(wx.EVT_MENU, self.OnExit, fileMenuExit)

        helpMenuAbout = helpmenu.Append(wx.ID_ABOUT,"About...","About clippy")
        self.Bind(wx.EVT_MENU, self.OnHelpAbout, helpMenuAbout)

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        menuBar.Append(helpmenu,"&Help") # Adding the "help" to the MenuBar

        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        # init database object
        self.db = clippyDB()

        # init the clipboard
        self.clipboard = clippyClipboard()

        # Create the main snippets tree (all snippets from today are shown)
        self.mainSnippetsTree = clippyMainSnippetsTree(self, self.db)

        # init the main thread
        self.clipboardThread = clippyClipboardThread(self, self.clipboard, self.db)
        self.clipboardThread.run()

        self.clipboardTimer = wx.Timer(self, wx.ID_ANY)
        self.clipboardTimer.Start(1000)
        self.Bind(wx.EVT_TIMER, self.clipboardThread.updateClipboard, self.clipboardTimer)

    def OnExit(self, event):
        self.tskic.Destroy()
        self.Destroy()

    def OnClose(self, event):
        #self.tskic.Destroy()
        self.Hide()

    def OnHelpAbout(self, event):
        dlg = wx.MessageDialog(self, "Created by Vali Dumitru\n\nvali.dumitru@webgearsoftware.com", "About", wx.OK|wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
