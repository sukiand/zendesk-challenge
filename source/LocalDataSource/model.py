#!usr/bin/env python

import json
import datetime
from source.LocalDataSource import _config

class Model:
    def __init__(self, data):
        payload = json.loads(data['payload'])
        self.timestamp = data['timestamp']
        self.attackerIP = payload['attackerIP']
        self.attackerPort = payload['attackerPort']
        self.victimIP = payload['victimIP']
        self.victimPort = payload['victimPort']

        self.downloadMethod = payload['downloadMethod'] if ('downloadMethod' in payload.keys()) else None
        self.attackerID = payload['attackerID'] if ('attackerID' in payload.keys()) else None
        self.vulName = payload['vulName'] if ('vulName' in payload.keys()) else None
        self.shellcodeName = payload['shellcodeName'] if ('shellcodeName' in payload.keys()) else None
            # self.downloadMethod = None
            # self.attackerID = None
            # self.vulName = None
            # self.shellcodeName = None
        self.connectionType = payload['connectionType']
        self.channel = data['channel']
        self.source = 'honeypot'

    def display(self):
        date = self.timestamp.strftime(_config.TIMEFORMAT)
        print _config.DISPLAY%(self.victimIP,
                               self.attackerIP,
                               self.victimPort,
                               self.attackerPort,
                               self.downloadMethod,
                               self.attackerID,
                               self.vulName,
                               self.shellcodeName,
                               self.connectionType,
                               self.source,
                               date)

