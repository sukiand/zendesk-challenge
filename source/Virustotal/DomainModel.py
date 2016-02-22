#!/usr/bin/env python

from source.Virustotal import _config

class Model:
    def __init__(self, domain, data):
        self.domain = domain
        self.response = data['response_code']
        if(self.response is 1):
            self.resolution_num = len(data['resolutions'])
            self.positives = 0;
            self.total = 0
            for record in data['detected_urls']:
                self.positives += record['positives']
                self.total +=record['total']

    def display(self):
        if(self.response is 1):
            print _config.DISPLAY_DOMAIN%(self.domain,
                                      self.resolution_num,
                                      self.positives,
                                      self.total,
                                      'Virustotal')
        else:
            print _config.DISPLAY_NOTFOUND%('domain',self.domain,'Virustotal')
