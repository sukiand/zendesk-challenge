#!/use/bin/env python

from source.DShield import _config

class Model:
    def __init__(self, data):
        self.data = data['ip']

    def display(self):
        print _config.DISPLAY_IP%(self.data['number'],
                                 self.data['count'],
                                 self.data['attacks'],
                                 self.data['asabusecontact'],
                                 self.data['asname'],
                                 self.data['ascountry'],
                                 'DShield'
                                 )

