from http.server import BaseHTTPRequestHandler, HTTPServer

port = 8888

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 헤더 시작
        self.send_response(200)
        # 중간부분 생략 가능
        self.send_header('Content-Type','text/html; charset=UTF-8')
        self.end_headers()
        # 헤더 끝

        # 바디 시작
        self.wfile.write('<h1>안녕하세요<h1>'.encode('utf-8'))


httpd = HTTPServer(('',port),MyHTTPRequestHandler)
print('Server running on port',port)
httpd.serve_forever()