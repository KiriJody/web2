from genericpath import exists
from http.server import HTTPServer, BaseHTTPRequestHandler

APP_HOST = '127.0.0.1'
APP_PORT = 55


class SimpleGetHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.end_headers()


    def do_GET(self):
        self._set_headers()
        n = 99
        self.wfile.write('<h1>{n}%</h1>'.format(n = n).encode("utf8"))


def run_server(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = (APP_HOST, APP_PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run_server(handler_class=SimpleGetHandler)
