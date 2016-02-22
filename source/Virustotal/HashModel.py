#!/usr/bin/env python

from source.Virustotal import _config

class Model:
    def __init__(self,hash, data):
        self.hash = hash
        self.response = data['response_code']
        if(self.response is 1):
            self.resource = data['resource']
            self.md5 = data['md5']
            self.sha1 = data['sha1']
            self.sha256 = data['sha256']
            self.positives = data['positives']
            self.total = data['total']
            self.scan_date = data['scan_date']

    def display(self):
        if(self.response is 1):
            print _config.DISPLAY_HASH%(self.hash,
                                      self.md5,
                                      self.sha1,
                                      self.sha256,
                                      self.positives,
                                      self.total,
                                      'Virustotal',
                                      self.scan_date
                                      )
        else:
            print _config.DISPLAY_NOTFOUND%('hash',self.hash,'Virustotal')
