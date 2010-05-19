#!/usr/bin/env python

import wx

class clippyMainSnippetsTree():
    def __init__(self, frame, db):
        self.doInit(frame, db)

    def doInit(self, frame, db):
        self.mainWindow = frame
        self.db = db
        self.tree = wx.TreeCtrl(self.mainWindow, size=(500,400))

        self.treeRoot = self.tree.AddRoot("Today's snippets")
        self.treeItems = self.db.GetTodaysSnippets()

        self.allItems = {}
        self.AddTreeNodes(self.treeRoot, self.treeItems, self.allItems)
        self.tree.Expand(self.treeRoot)
        self.lastUsedItem = None

        self.treeSizer = wx.BoxSizer(wx.VERTICAL)
        self.treeSizer.Add(self.tree, 1, wx.EXPAND, 0)
        self.mainWindow.SetSizer(self.treeSizer)
        self.treeSizer.Fit(self.mainWindow)
        self.mainWindow.Layout()

    def AddTreeNodes(self, parentItem, items, holder):
        for item in items:
            if type(item) == str or type(item) == unicode:
                elem = self.tree.AppendItem(parentItem, item)
                self.mainWindow.Bind(wx.EVT_TREE_ITEM_RIGHT_CLICK, self.OnNodeRightClick, self.tree)
                holder[str(elem)] = item
            else:
                newItem = self.tree.AppendItem(parentItem, item[0])
                self.AddTreeNodes(newItem, item[0])

    def GetItemText(self, item):
        if item:
            return self.tree.GetItemText(item)
        else:
            return ""

    def OnNodeRightClick(self, event):
        self.lastUsedItem = event.GetItem()

        menu = wx.Menu()
        menu.Append(1, "Use")
        menu.Bind(wx.EVT_MENU, self.OnMenuCopySelection)
        self.mainWindow.PopupMenu(menu, event.GetPoint())

    def OnMenuCopySelection(self, event):
        if self.lastUsedItem is not None:
            currentlySelectedItemString = self.tree.GetItemText(self.lastUsedItem)

            self.mainWindow.clipboard.updateWithText(currentlySelectedItemString)

        #print self.allItems[str(self.lastUsedItem)]
