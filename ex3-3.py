#POST 방식 요청

from urllib.parse import urlencode
from urllib.request import Request, urlopen

data=urlencode({'name':'둘리','a':10,'b':20})
print(data,'\n')
data=data.encode("UTF-8") #바이트 형태로 보내야 하므로 인코딩 필요
print(data)

req=Request('http://www.example.com',data)
req.add_header('Contest-Type','text/html')

f = urlopen(req)
req=f.read()

print(req)