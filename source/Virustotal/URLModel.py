#!/usr/bin/env python

from source.Virustotal import _config

class Model:
    def __init__(self, URL, data):
        self.url = URL
        self.response = data['response_code']
        if(self.response is 1):
            self.resource = data['resource']
            self.positives = data['positives']
            self.total = data['total']
            self.scan_date = data['scan_date']

    def display(self):
        if(self.response is 1):
            print _config.DISPLAY_URL%(self.url,
                                      self.resource,
                                      self.positives,
                                      self.total,
                                      'Virustotal',
                                      self.scan_date
                                      )
        else:
            print _config.DISPLAY_NOTFOUND%('url',self.url,'Virustotal')
