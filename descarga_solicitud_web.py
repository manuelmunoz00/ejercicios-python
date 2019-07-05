import requests
import hashlib
import re

#r=requests.session()
print("Trayendo datos-requests");
url='http://domain:puerto/';
r=requests.get(url);

#print(r.text)
texto=r.text
buscar='h3'

start = texto.find('<h3 align=\'center\'>')+19
#print(start)
end = texto.find('</h3>', start)
#print(end)
dato=texto[start:end]
print(dato)
md5=(hashlib.md5(dato.encode('utf-8')).hexdigest())
data = {'hash':md5}
r = requests.post(url=url, data=data)
print (r.text)
