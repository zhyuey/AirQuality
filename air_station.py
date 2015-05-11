# -*- coding:utf-8 -*- #
import urllib.request
import sys

def getdata():
    url="http://113.108.142.147:20035/emcpublish/ClientBin/Env-CnemcPublish-RiaServices-EnvCnemcPublishDomainService.svc/binary/GetAQIDataPublishLives"
    data=urllib.request.urlopen(url).read()
    mystr = data.decode('latin-1')
    return mystr



if len(sys.argv) < 2:
    filename = "dd4.txt"
else:
    filename = sys.argv[1]
myfile=open(filename, "w", encoding="latin-1")

myfile.write(getdata())
myfile.close()
