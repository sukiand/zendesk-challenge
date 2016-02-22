#!/usr/bin/env python

from source.Google import _config

class Model:
    def __init__(self, url, type):
        self.url = url
        self.type = type if (type) else 'None'

    def display(self):
        print _config.DISPLAY%(self.url,self.type,'Google Safe Browsing')

