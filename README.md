### Information
This is a simple python program to solve zendesk challenge program. Search Indicators of Compromise(IOC) in several data sources.

- local data source  
JSON data provided by zendesk. Stored in mongodb. Support searching commands: ip, port, url, domain, file, hash, and multiple search.
- [DSheild](https://isc.sans.edu/api/)  
Public API. Support searching commands: ip, port
- [Virustotal](https://www.virustotal.com/en/documentation/public-api/)  
API key needed. Support searching commands: ip, domain, url, hash
- [Google Safe Browsing](https://developers.google.com/safe-browsing/?csw=1)  
API key needed. Support searching commands: url

### Author
Changyun Gong.

### Setup

#### develop environment
python 2.7.6  
ubuntu 14.04  
mongoDB 3.0.6  

1 import the JSON to mongoDB
```bash
cd HOME_DIR/source/LocalDataSource/database
chmod +x database.sh
./database.sh
```
you can change the parameters in database.sh, to import to the right place.
```bash
vim HOME_DIR/source/LocalDataSource/_config.py
```

2 fill in your own keys
```bash
vim HOME_DIR/source/Virustotal/_config.py
vim HOME_DIR/source/Google/_config.py
```

### program
This program use python cmd module as shell. Dynamically load modules in `./source` folder to search IOC.
launch the program:
```bash
python main.py
```

#### commands
ip ip_address [-s source]  
port port_num [-s source]  
url urls [-s source]  
domain domain_names [-s source]  
file file_names [-s source]  
hash hash_values [-s source]  
search [-i ip_address] [-p port] [-d domain] [-u urls] [-f file_names] [-h hash_values] [-s source]  

#### examples
```bash
(cmd)ip 70.91.145.10 172.31.13.121
(cmd)ip 90.156.201.27 -s Virustotal
(cmd)port 8080 44937 -s DShield
(cmd)url http://www.dj3344.com/  -s Google
(cmd)url http://Fianfette.org/ -s Google
(cmd)url http://www.google.com
(cmd)hash 99017f6eebbac24f351415dd410d522d
(cmd)domain 027.ru -s Virustotal
(cmd)search -i 192.168.0.1 172.31.13.121 172.31.13.124 -p 8080 47452
```


