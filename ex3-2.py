#GET 방식 요청

from urllib.parse import urlencode
from urllib.request import urlopen

query=urlencode({'name':'또치','a':10,'b':20})

f=urlopen('http://www.example.com?' + query)
response=f.read()
print(response)