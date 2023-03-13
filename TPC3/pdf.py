#!/usr/bin/env python3
import html
import os

class PDF:
    def __init__(self):
        pass

    def setHtml(self, html):
        self.html = html

    def flushHtml(self, target=None):
        if target == None:
            target = "default.pdf"
        print(target)
        os.system("pandoc " + self.html + " -o " + target)
