from http.client import HTTPConnection


#1 연결
connection=HTTPConnection('www.example.com')

#2 요청보내기
connection.request('GET','/') # '/'만써주면 웹에 설정되어있는 default문서 받아옴
# GET방식으로 받아옴

#3 응답받기
response = connection.getresponse()
print(response.status,response.reason)

#4 Body읽어오기
body = response.read()
print(body)

#
# 404 에러 받아보기
#
connection.request('GET','/babo.html')
response=connection.getresponse()
print(response.status, response.reason)