"""
search according to the DShield API.
use python requests module to send HTTP GET request
"""
#!/usr/bin/env python

import config
from source.DShield import _config, IPModel, PortModel
import requests

class DShield:
    def search(self, IOC):
        result = []
        if(len(IOC.keys()) is not 1):
            return
        key = IOC.keys()[0]
        if key not in _config.SUPPORTED_IOC:
            return
        if(key is 'ip'):
            for item in IOC[key]:
                try:
                    r = requests.get(_config.URL['ip']%item)
                    a = IPModel.Model(r.json())
                    result.append(a)
                except:
                    print 'network problem'
        if(key is 'port'):
            for item in IOC[key]:
                try:
                    r = requests.get(_config.URL['port']%item)
                    a = PortModel.Model(r.json())
                    result.append(a)
                except:
                    print 'network problem'
        for item in result:
            item.display()

