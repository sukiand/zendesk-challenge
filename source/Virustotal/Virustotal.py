"""
search based on virustotal API
"""
#!/usr/bin/env python

from source.Virustotal import _config, IPModel, URLModel, HashModel, DomainModel
import urllib
import requests

class Virustotal:
    def search(self,IOC):
        for key in IOC.keys():
            if key not in _config.SUPPORTED_IOC:
                continue
            url_part = key
            paras_part = 'resource'
            if key is 'ip':
                url_part = 'ip-address'
                paras_part = 'ip'
            elif key is 'hash':
                url_part = 'file'
            elif key is 'domain':
                paras_part = 'domain'
            result = []
            for item in IOC[key]:
                paras = {paras_part:item,'apikey':_config.KEY}
                url = ('%s?%s')%(_config.SOURCEPATH%(url_part),urllib.urlencode(paras))
                # print url
                try:
                    r = requests.get(url)
                    if(key is 'ip'):
                        a = IPModel.Model(item, r.json())
                    elif(key is 'url'):
                        a = URLModel.Model(item,r.json())
                    elif(key is 'hash'):
                        a = HashModel.Model(item, r.json())
                    elif(key is 'domain'):
                        a = DomainModel.Model(item, r.json())
                    result.append(a)
                except:
                    print _config.NETWORKERROR
            for item in result:
                item.display()
