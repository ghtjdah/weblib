from urllib.parse import urlparse

result=urlparse('http://www.python.org:80/guido/python.html?name=둘리&id=dooly#fucking')
print(result,type(result))
print(list(result))
print(tuple(result))
print(result.scheme,result.netloc)