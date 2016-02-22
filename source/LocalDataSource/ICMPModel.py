#!usr/bin/env python

import json
import datetime
from source.LocalDataSource import _config

class Model:
    def __init__(self, data):
        payload = json.loads(data['payload'])
        self.timestamp = data['timestamp']
        self.destinationIP = payload['destination_ip']
        self.sourceIP = payload['source_ip']
        self.signature = payload['signature']
        self.classification = payload['classification']
        self.channel = data['channel']
        self.source = 'honeypot'

    def display(self):
        date = self.timestamp.strftime(_config.TIMEFORMAT)
        print _config.DISPLAY_ICMP%(self.destinationIP,
                               self.sourceIP,
                               self.classification,
                               self.signature,
                               self.channel,
                               self.source,
                               date)

