import requests
from bs4 import BeautifulSoup
import hashlib

r=requests.session()
url='http://docker.hackthebox.eu:37591/';
resp=r.get(url);
class2=BeautifulSoup(resp.text, 'lxml').h3.string
print(class2)
md5=(hashlib.md5(class2.encode()).hexdigest())
print(md5)
res1 = r.post(url=url, data={'hash':md5})
#print (dir(re))
print (res1.text)
#help(res1)
