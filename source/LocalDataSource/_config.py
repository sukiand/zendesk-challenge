#!usr/bin/env python

import config

# change the mongodb config according to your own situation
MONGOURL = 'mongodb://localhost:27017/'

TIMEFORMAT = config.TIMEFORMAT

DISPLAY = 'Victim IP: %s\n\
          \rAttacker IP: %s\n\
          \rVictim Port: %s\n\
          \rAttacker Port: %s\n\
          \rDownload Method: %s\n\
          \rAttacker ID: %s\n\
          \rVulnerable Name: %s\n\
          \rShellCode Name: %s\n\
          \rConnection Type: %s\n\
          \rSource: %s\n\
          \rTime Stamp: %s\n'

DISPLAY_PATTERN = 'Pattern: %s\n\
                 \rFile: %s\n\
                 \rRequest: %s\n\
                 \rURL: %s\n\
                 \rChannel: %s\n\
                 \rSource: %s\n\
                 \rTime Stamp: %s\n'

DISPLAY_ICMP = 'Destination IP: %s\n\
               \rSource IP: %s\n\
               \rClassification: %s\n\
               \rSignature: %s\n\
               \rChannel: %s\n\
               \rSource: %s\n\
               \rTime Stamp: %s\n'
