#!/usr/bin/env python

import config

TIMEFORMAT = config.TIMEFORMAT

SUPPORTED_IOC = ['url',]

SOURCEPATH = 'https://sb-ssl.google.com/safebrowsing/api/lookup'

NETWORKERROR = 'network error, please try again for google source'

# change the key to your own!!
# I cannot expose my key to the public..
QUERY = {
        'client':'changyun',
        'appver':'1.0',
        'key':'change to your key',
        'pver':'3.1',
        'url':' ',
        }

DISPLAY = 'url: %s\n\
          \rType: %s\n\
          \rSource: %s\n'

