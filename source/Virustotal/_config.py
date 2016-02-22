#!/usr/bin/env python

import config

TIMEFORMAT = config.TIMEFORMAT

SUPPORTED_IOC = ['ip','url','domain', 'hash' ]

SOURCEPATH = 'https://www.virustotal.com/vtapi/v2/%s/report'

# change this to your own key of virustotal
KEY = 'change to your key'

NETWORKERROR = 'network error, please try again for virustotal source'

DISPLAY_IP = 'IP: %s\n\
             \rResolution times: %s\n\
             \rPositives scan times: %s\n\
             \rTotal scan time: %s\n\
             \rSource: %s\n'

DISPLAY_DOMAIN = 'Domain: %s\n\
             \rResolution times: %s\n\
             \rPositives scan times: %s\n\
             \rTotal scan time: %s\n\
             \rSource: %s\n'

DISPLAY_URL = 'url: %s\n\
             \rResource: %s\n\
             \rPositives scan times: %s\n\
             \rTotal scan time: %s\n\
             \rSource: %s\n\
             \rScan date: %s\n'

DISPLAY_HASH = 'Hash: %s\n\
             \rmd5: %s\n\
             \rsha1: %s\n\
             \rsha256:%s \n\
             \rPositives scan times: %s\n\
             \rTotal scan time: %s\n\
             \rSource: %s\n\
             \rScan date: %s\n'

DISPLAY_NOTFOUND = '%s: %s\n\
                   \rNOT FOUND\n\
                   \rSource: %s\n'

