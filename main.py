"""
This file provide the shell of the program. Python cmd module is applied.
each command has three corresponding functions:
    do_command: deal with user input, split the parameters
    complete_command: auto-complete when user is typeing words.
    help_command: provide help document. 'help + command'

This file also contains customized functions to deal with user input, such as validIP, validPort,
to check if the parameters are valid.

Generally:
    input: user input, string (commands and parameters)
    output: a search object IOC and a list of resources
    eg: IOC = {'ip' = ['xxx.xxx.xxx.xxx', 'xxx.xxx.xxx.xxx'], 'port' = [..], ..}
        source = ['local_data_source']
"""
#!usr/bin/env python

from cmd import Cmd
import signal
import config
import socket
from search import Search

class Command(Cmd):
    intro = ('%s\n%s\n%s')%(config.HELP['intro'],config.HELP['help'],config.HELP['exit'])

    def cmdloop(self):
        try:
            Cmd.cmdloop(self)
        except KeyboardInterrupt as e:
            print ''
            self.exit()

    def do_ip(self,line):
        source = config.COMMAND_DEFAULT_SOURCE['ip']
        commands = line.strip().split('-',1)
        validIpList = []
        for command in commands:
            if(command.startswith('s ')):
                source = self.validSource('ip',command[1:])
            else:
                if not command:
                    print config.ERROR['paras_needed']%('ip')
                    return
                validIpList = self.validIP(command)
        if(validIpList):
            Search(IOC = {'ip':validIpList},source = source)

    def help_ip(self):
        print config.HELP['command']%('ip','ip_address')
        print config.HELP['extra']

    def complete_ip(self, text, line, begidx, endidx):
        if text:
            return [source
                    for source in config.COMMAND_DEFAULT_SOURCE['ip']
                    if source.startswith(text)]
        else:
            return config.SOURCE

    def do_port(self,line):
        source = config.COMMAND_DEFAULT_SOURCE['port']
        commands = line.strip().split('-',1)
        validPortList = []
        for command in commands:
            if(command.startswith('s ')):
                source = self.validSource('port',command[1:])
            else:
                if not command:
                    print config.ERROR[paras_needed]%('port')
                    return
                validPortList = self.validPort(command)
        if(validPortList):
            Search(IOC = {'port':validPortList}, source = source)

    def complete_port(self, text, line, begidx, endidx):
        if text:
            return [source
                    for source in config.COMMAND_DEFAULT_SOURCE['port']
                    if source.startswith(text)]
        else:
            return config.SOURCE

    def help_port(self):
        print config.HELP['command']%('port','port_number')
        print config.HELP['extra']


    def do_file(self, line):
        source = config.COMMAND_DEFAULT_SOURCE['file']
        commands = line.strip().split('-',1)
        file_list = []
        for command in commands:
            if(command.startswith('s ')):
                source = self.validSource('file',command[1:])
            else:
                if not command:
                    print config.ERROR[paras_needed]%('filename')
                    return
                file_list = command.strip().split(' ')
        if(file_list):
            Search(IOC = {'file':file_list},source = source)

    def complete_file(self, text, line, begidx, endidx):
        if text:
            return [source
                    for source in config.COMMAND_DEFAULT_SOURCE['file']
                    if source.startswith(text)]
        else:
            return config.SOURCE

    def help_file(self):
        print config.HELP['command']%('file','file_name')
        print config.HELP['extra']

    def do_url(self, line):
        source = config.COMMAND_DEFAULT_SOURCE['url']
        commands = line.strip().split('-',1)
        url_list = []
        for command in commands:
            if(command.startswith('s ')):
                source = self.validSource('url',command[1:])
            else:
                if not command:
                    print config.ERROR['paras_needed']%('url')
                    return
                url_list = command.strip().split(' ')
        if(url_list):
            Search(IOC = {'url':url_list},source = source)

    def complete_url(self, text, line, begidx, endidx):
        if text:
            return [source
                    for source in config.COMMAND_DEFAULT_SOURCE['url']
                    if source.startswith(text)]
        else:
            return config.SOURCE

    def help_url(self):
        print config.HELP['command']%('url','urls')
        print config.HELP['extra']

    def do_domain(self, line):
        source = config.COMMAND_DEFAULT_SOURCE['domain']
        commands = line.strip().split('-',1)
        domain_list = []
        for command in commands:
            if(command.startswith('s ')):
                source = self.validSource('domain',command[1:])
            else:
                if not command:
                    print config.ERROR['paras_needed']%('domain')
                    return
                domain_list = command.strip().split(' ')
        if(domain_list):
            Search(IOC = {'domain':domain_list},source = source)

    def complete_domain(self, text, line, begidx, endidx):
        if text:
            return [source
                    for source in config.COMMAND_DEFAULT_SOURCE['domain']
                    if source.startswith(text)]
        else:
            return config.SOURCE

    def help_domain(self):
        print config.HELP['command']%('domain','domain_names')
        print config.HELP['extra']

    def do_hash(self, line):
        source = config.COMMAND_DEFAULT_SOURCE['hash']
        commands = line.strip().split('-',1)
        hash_list = []
        for command in commands:
            if(command.startswith('s ')):
                source = self.validSource('hash',command[1:])
            else:
                if not command:
                    print config.ERROR['paras_needed']%('hash_values')
                    return
                hash_list = command.strip().split(' ')
        if(hash_list):
            Search(IOC = {'hash':hash_list},source = source)

    def complete_hash(self, text, line, begidx, endidx):
        if text:
            return [source
                    for source in config.COMMAND_DEFAULT_SOURCE['hash']
                    if source.startswith(text)]
        else:
            return config.SOURCE

    def help_hash(self):
        print config.HELP['command']%('hash','hash_values')
        print config.HELP['extra']

    def do_search(self, line):
        IOC = {}
        sourceList = config.SOURCE
        commands = line.strip(' ').split('-')
        # print commands
        for command in commands:
            # print command
            if command is '':
                continue
            if command is ' ':
                continue
            paras = command.strip().split(' ',1)
            if(paras[0].startswith('i')):
                if(paras[1]):
                    validIPList = self.validIP(paras[1])
                    if(validIPList):
                        IOC['ip'] = validIPList 
                else:
                    print config.ERROR[paras_needed]%('ip addresses')
            elif(paras[0].startswith('p')):
                if(paras[1]):
                    validPortList = self.validPort(paras[1])
                    if(validPortList):
                        IOC['port'] = validPortList
                else:
                    print config.ERROR['paras_needed']%('port')
            elif(paras[0].startswith('u')):
                if(paras[1]):
                    IOC['url'] = paras[1].strip().split(' ')
                else:
                    print config.ERROR['paras_needed']%('url')
            elif(paras[0].startswith('d')):
                if(paras[1]):
                    IOC['domain'] = paras[1].strip().split(' ')
                else:
                    print config.ERROR['paras_needed']%('domain')
            elif(paras[0].startswith('f')):
                if(paras[1]):
                    IOC['file'] = paras[1].strip().split(' ')
                else:
                    print config.ERROR['paras_needed']%('file')
            elif(paras[0].startswith('h')):
                if(paras[1]):
                    IOC['hash'] = paras[1].strip().split(' ')
                else:
                    print config.ERROR['paras_needed']%('file')
            elif(paras[0].startswith('s')):
                if(paras[1]):
                   sourceList = self.validSource(paras[1])
                else:
                    print config.ERROR['paras_needed']%('source')
            else:
                print config.ERROR['invalid_command']
        # print IOC
        Search(IOC = IOC, source = sourceList)
        return

    def complete_search(self, text, line, begidx, endidx):
        if text:
            return [source
                    for source in config.SOURCE
                    if source.startswith(text)]
        else:
            return config.SOURCE

    def help_search(self):
        print config.HELP['search']
        print config.HELP['extra']

    def do_exit(self,line):
        self.exit()

    def help_exit(self):
        print config.HELP['exit']

    def exit(self):
        print('bye~')
        return -1;

    def validIP(self, line):
        ipList = line.strip().split(' ')
        validIpList = []
        for ip in ipList:
            try:
                socket.inet_aton(ip)
                if(ip.count('.') is 3):
                    validIpList.append(ip)
                else:
                    print config.ERROR['invalid_paras']%(ip,'ip address')
            except:
                print config.ERROR['invalid_paras']%(ip,'ip address')
        return validIpList

    def validPort(self,line):
        portList = line.strip().split(' ')
        validPortList = []
        for port in portList:
            try:
                pn = int(port)
                validPortList.append(pn)
            except:
                print config.ERROR['invalid_paras']%(port,'port')
        return validPortList

    def validSource(self,command, line):
        sourceList = line.strip().split(' ')
        validSource = []
        for source in sourceList:
            if source in config.COMMAND_DEFAULT_SOURCE[command]:
                validSource.append(source)
            else:
                print config.ERROR['invalid_source']%(source)
        return validSource



if __name__ == '__main__':
    Command().cmdloop()


