#!/usr/bin/env python

from source.DShield import _config

class Model:
    def __init__(self, data):
        self.port = data['number']
        self.records = data['data']['records'] if('records' in data['data'].keys()) else 'None'
        self.targets = data['data']['targets'] if('targets' in data['data'].keys()) else 'None'
        self.sources = data['data']['sources'] if('sources' in data['data'].keys()) else 'None'
        self.services = data['services']

    def display(self):
        print _config.DISPLAY_PORT%(self.port,
                                    self.records,
                                    self.targets,
                                    self.sources,
                                    self.services['udp']['service'],
                                    self.services['udp']['name'],
                                    self.services['tcp']['service'],
                                    self.services['tcp']['name'],
                                    'DShield'
                                    )
