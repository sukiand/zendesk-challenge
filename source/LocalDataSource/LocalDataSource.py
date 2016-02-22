"""
Seach in local data source(mongodb).
There are several data model in the honeypot.json. Main difference is the payload. 
So there would be three different data models, and remains are unsupported.

"""
#!usr/bin/env python

from source.LocalDataSource import _config, model, patternModel, ICMPModel
from pymongo import MongoClient

class LocalDataSource:
    def __init__(self):
        self.result = []
        self.flag = False
        try:
            client = MongoClient(_config.MONGOURL)
            self.flag = True
        except:
            print 'error to connect to mongodb'
            return
        db = client.zendesk
        self.coll = db.honeypot

    def search(self, IOC):
        if( not self.flag):
            print 'error to connect to mongodb'
            return
        query = {'$and': []}
        for key in IOC.keys():
            tmp = {'$or':[]}
            for item in IOC[key]:
                if type(item) is not str:
                    item = str(item)
                expression = {'payload': {'$regex': item }}
                tmp['$or'].append(expression)
            query['$and'].append(expression)
        cursor = self.coll.find(query)

        for document in cursor:
            if(document['payload'].find('attackerIP')>0):
                a = model.Model(document)
                a.display()
            elif(document['payload'].find('pattern')>0):
                a = patternModel.Model(document)
                a.display()
            elif(document['payload'].find('ICMP')>0):
                a = ICMPModel.Model(document)
                a.display()
            else:
                print 'unsupported data model'



