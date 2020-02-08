import http.server
import socketserver

PORT = 8000

class httpServer(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory = "public", **kwargs)
        
    def do_GET(self):
        super().do_GET()

Handler = httpServer;

if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()