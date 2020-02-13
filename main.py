# main hotel manager webserver 
import sys
import os
from cgi import parse_header
import http.server
from http.server import HTTPServer, _url_collapse_path
import socketserver
# os.path.join(os.path.dirname(os.path.abspath(__file__)), 'public\cgi-bin')
# print("os.path:{}".format(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'public\cgi-bin'))) # os.path:F:\LAB\projects\hotels-python\public\cgi-bin
# from public.htbin.session import isSession

PORT = 8000

class httpServer(http.server.CGIHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory = "public", **kwargs)

    def do_GET(self):
        super().do_GET()
        # self.parse_request()
        # print('path:{}'.format(self.path)) # path:/index.html
        # print('command:{}'.format(self.command)) # command:GET
        # if self.path == '/login.html':
        #     super().do_GET()

        # # list of headers
        # # for header in self.headers:
        # #   print('header: {}'.format(header))  
        # if "Cookie" in self.headers:
        #     key, pdict = parse_header(self.headers['Cookie'])
        #     sid = 'none'
        #     if 'sid' in pdict:
        #         sid = pdict['sid']
        #     if isSession(sid):
        #         super().do_GET()
        #         return
        # self.send_header("Location", 'login.html')
        # self.end_headers()
        # print('end')

    
Handler = httpServer;

if __name__ == '__main__':
    httpd = HTTPServer(("", PORT), Handler)
    print("serving at port", PORT)
    httpd.serve_forever()
