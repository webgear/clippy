#!/usr/bin/env python

import wx
import sqlite3
import time
import datetime

class clippyDB():
    def __init__(self):
        # connect to db and do stuff here...
        self.dbConnection = sqlite3.connect('clippy.sqlite')
        self.dbCursor = self.dbConnection.cursor()

    def ClipExists(self, snippet):
        dbArgs = (snippet,)
        cnt = None

        self.dbCursor.execute('SELECT COUNT(cs_id), cs_id, cs_snippet FROM clipboard_snippets WHERE cs_snippet=?', dbArgs)

        for item in self.dbCursor:
            cnt = item

        self.dbCursor.close()

        return cnt

    def CreateClip(self, text):
        dbArgs = (text,)
        self.dbCursor.execute('INSERT INTO clipboard_snippets(cs_snippet) VALUES(?)', dbArgs)
        self.dbConnection.commit()

        self.dbCursor.close()

    def UpdateClip(self, id, newText):
        dbArgs = (id,newText,)

        if newText != None:
            self.dbCursor.execute('UPDATE clipboard_snippets SET cs_snippet=? WHERE cs_id=?', dbArgs)
            self.dbConnection.commit()
            self.dbCursor.close()

    def GetTodaysSnippets(self):
        self.dbCursor.execute('SELECT cs_snippet FROM clipboard_snippets WHERE cs_created_at >= strftime("%Y-%m-%d 00:00:00", "now") ORDER BY cs_created_at DESC')

        items = []

        for item in self.dbCursor:
            items.append(item[0])

        self.dbCursor.close()

        return items
