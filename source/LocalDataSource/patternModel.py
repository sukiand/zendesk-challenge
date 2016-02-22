#!usr/bin/env python

import json
import datetime
from source.LocalDataSource import _config

class Model:
    def __init__(self, data):
        payload = json.loads(data['payload'])
        self.timestamp = data['timestamp']
        self.pattern = payload['pattern']
        self.source = payload['source']
        self.file = payload['filename']
        self.request = payload['request_raw']
        self.url = payload['request_url']
        self.channel = data['channel']
        self.source = 'honeypot'

    def display(self):
        date = self.timestamp.strftime(_config.TIMEFORMAT)
        print _config.DISPLAY_PATTERN%(self.pattern,
                               self.file,
                               self.request,
                               self.url,
                               self.channel,
                               self.source,
                               date)

