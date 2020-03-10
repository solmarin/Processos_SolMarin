from http.server import  BaseHTTPRequestHandler, HTTPServer

class http_server:
    def __init__(self):
        server = HTTPServer(('', 8080), myHandler)
        server.serve_forever()

class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if '/practica.html' in self.path:
            fichero = open(self.path[1:]).read()
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(bytes(fichero, 'utf8'))
        else:
            self.send_error(404,'Not Found','Esta pagina no funciona si no pones /practica.html. Jordi ponme un 10.')

class main:
    def __init__(self):
        self.server = http_server()

if __name__ == '__main__':
    main()
