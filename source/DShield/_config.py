#!/usr/bin/env python

import config

TIMEFORMAT = config.TIMEFORMAT

SUPPORTED_IOC = ['ip','port']

SOURCEPATH = 'https://isc.sans.edu/api/'

URL = {
        'ip':SOURCEPATH+'ip/%s?json',
        'port':SOURCEPATH+'port/%s?json'
        }

DISPLAY_IP = 'IP: %s\n\
             \rcount: %s\n\
             \rattacks: %s\n\
             \rabuse contact: %s\n\
             \ras name: %s\n\
             \ras country: %s\n\
             \rsource: %s\n'

DISPLAY_PORT = 'Port: %s\n\
               \rrecordes: %s\n\
               \rtargets: %s\n\
               \rsources: %s\n\
               \rUDP:\n\
               \r\tservice: %s\n\
               \r\tname: %s\n\
               \rTCP:\n\
               \r\tservice:%s\n\
               \r\tname:%s\n\
               \rsource: %s\n'
