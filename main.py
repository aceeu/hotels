import http.server
from http.server import HTTPServer
import socketserver

PORT = 8000

class httpServer(http.server.CGIHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory = "public", **kwargs)
        
Handler = httpServer;

if __name__ == '__main__':
    httpd = HTTPServer(("", PORT), Handler)
    httpd.cgi_directories = "cgi-bin"
    print("serving at port", PORT)
    httpd.serve_forever()
