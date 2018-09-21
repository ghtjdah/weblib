from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

port=7777

class MyHTTPRequestHandler(BaseHTTPRequestHandler):

    def get_params(self,name):
        querystream=self.path[self.path.find('?')+1:]
        parmes=parse_qs(querystream)
        value = parmes.get(name)

        '''if(value is None):
            return None
        else:
            return value.pop()'''

        return '' if(value is None) else value.pop()
        #자바에서코드
        #return (value is None) ? None : value.pop()

    def ex1(self):
        # 헤더 시작
        self.send_response(200)
        # 중간부분 생략 가능
        self.send_header('Content-Type', 'text/html; charset=UTF-8')
        self.end_headers()
        # 헤더 끝

        # 바디 시작
        self.wfile.write("<h1>iot's TEST ex1<h1>".encode('utf-8'))

    def ex2(self):
        # 헤더 시작
        self.send_response(200)
        # 중간부분 생략 가능
        self.send_header('Content-Type', 'text/html; charset=UTF-8')
        self.end_headers()
        # 헤더 끝

        # 바디 시작
        self.wfile.write("<h1>iot's TEST ex2<h1>".encode('utf-8'))


    def do_GET(self):
        index=self.path.find('?')
        if(index == -1):
            req_url = self.path
        else:
            req_url=self.path[:index]

        #URL Mapping
        if(req_url=='/iot'):
            hadler_name='ex'+self.get_params('ex')
            print(MyHTTPRequestHandler.__dict__)
            if(hadler_name not in MyHTTPRequestHandler.__dict__):
                self.send_error(404,'File Not Found Params')
                return

            MyHTTPRequestHandler.__dict__[hadler_name](self)

        elif(req_url=='/board'):
            # 헤더 시작
            self.send_response(200)
            # 중간부분 생략 가능
            self.send_header('Content-Type', 'text/html; charset=UTF-8')
            self.end_headers()
            # 헤더 끝

            # 바디 시작
            self.wfile.write("<h1>board's TEST<h1>".encode('utf-8'))
        else:
            self.send_error(404,'File Not Found PATH')
            #return


httpd = HTTPServer(('',port),MyHTTPRequestHandler)
print('Server running on port',port)
httpd.serve_forever()
