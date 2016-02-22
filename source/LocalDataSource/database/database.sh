#!/bin/sh

# import the honeypot.json to mongodb. change the parameters according to your own situation

mongoimport --db zendesk --collection honeypot --drop --file ./honeypot.json --host=127.0.0.1;

