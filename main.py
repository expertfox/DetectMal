
import re
import os

MalWord = "MALWARE"

with open('requestList.txt') as f:
    requests = f.readlines()

    for req in requests:
        if req.find(MalWord):
            IPADRRESS = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', req).group()

            print(IPADRRESS)

            os.system('iptables -A INPUT -s '+ IPADRRESS + '-p tcp --destination -port 80 -j DROP')
            os.system('iptables -A INPUT -s' + IPADRRESS + '-p tcp --destination -port 443 -j DROP')
