"""
dynamically import all the modules from source folder, record them in a map.
Call the module when IOC is need to be found from that data source.

    input: search object IOC, data source list
    output: call each search() function in each data source module.

"""
#!usr/bin/env python

import config
g_source = {}
for s in config.SOURCE:
    module_path = '%s.%s.%s'%(config.SOURCEPATH,s,s)
    new_module = __import__(module_path, globals(), locals(), [s],-1)
    func = getattr(new_module,s)()
    g_source[s] = func

class Search:
    def __init__(self,IOC,source = config.SOURCE):
        for item in source:
            g_source[item].search(IOC)
