"""
provide config for the whole project, mainly for main.py
format of outputs and some global variables.
"""
#!usr/bin/env python

# data source from 4 places. local database: mongodb(honeypot.json imported), and 3 api: DShield, google safe browser and virustotal
SOURCE = ['LocalDataSource','DShield','Google','Virustotal']
# the folder contains data sources.
SOURCEPATH = 'source'
# all the IOC, supported to be quired in the program
IOC = ['ip', 'port', 'domain','url', 'file','hash']

# define the default data source set for each command. 
COMMAND_DEFAULT_SOURCE = {
        'ip':['LocalDataSource','DShield','Virustotal'],
        'port':['LocalDataSource','DShield'],
        'domain':['LocalDataSource','Virustotal'],
        'url':['LocalDataSource','Google','Virustotal'],
        'file':['LocalDataSource',],
        'hash':['LocalDataSource','Virustotal'],
        'search':['LocalDataSource']
        }

# time format for data output.
TIMEFORMAT = '%Y-%m-%d %H:%M:%S'
# TIMEFORMAT = '%Y-%m-%d'
# TIMEFORMAT = '%m/%d/%Y'

WELCOME = '\n\r************************************\n\
          \r welcome to zendesk challenge shell\n\
          \r\t\t---by Changyun Gong\n\
          \r************************************\n'

HELP = {
        'intro': WELCOME,
        'command':'%s %s [-s sources]',
        'search':'search [-i ip_address] [-p port] [-d domain] [-u url] [-f file_name] [-h hash_value] [-s sources]',
        'exit': 'type "exit" or Ctrl+c to exit the program',
        'help': 'type "help" or "?" to get commands\n\
                \rtype "help/?" [command] to get detail information',
        'extra': 'command and sources can be auto-complete with <tab>'
        }

ERROR = {
        'paras_needed':'more parameters are needed, type "help/? %s" for more information',
        'invalid_paras': '%s is not a valid %s',
        'invalid_command': 'no such command',
        'invalid_source': '%s source is not supported now'
        }

