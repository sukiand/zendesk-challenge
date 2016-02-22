"""
search based on google safe browser API
"""
#!/usr/bin/env python

from source.Google import _config, model
import requests
import urllib

class Google:
    def search(self, IOC):
        if(len(IOC.keys()) is not 1):
            return
        key = IOC.keys()[0]
        if key is not 'url':
            return

        result = []

        for item in IOC[key]:
            url = item.encode('utf-8')
            encoded_url = urllib.quote(url, safe='')
            _config.QUERY['url'] = encoded_url
            # print _config.URL['url']%(encoded_url)
            query = urllib.urlencode(_config.QUERY)
            # print ('%s?%s'%(_config.SOURCEPATH,query))
            try:
                r = requests.get('%s?%s'%(_config.SOURCEPATH,query))
                if(r.status_code < 300):
                    a = model.Model(item,r.text)
                    result.append(a)
                else:
                    print _config.NETWORKERROR 
            except:
                print _config.NETWORKERROR 
        for item in result:
            item.display()



