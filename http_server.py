# from http.server import HTTPServer, BaseHTTPRequestHandler
# #
# HOST = ''

PORT = 9000
#server_address = List['http://127.0.0.1',9000]
# class RequestHander(BaseHTTPRequestHandler):
#     def do_Post(self):
#         payload_size = int(self.headers['Content-Length'])
#         payload = self.rfile.read(payload_size)
#         self.send_response(200)
#         self.end_headers()
#         self.wfile.write(payload)
#
#
# server = HTTPServer(('',9500), RequestHander)
# server.serve_forever()
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_headers()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        self._set_headers()
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        # content_len = int(self.headers.get('content-length', 0))
        # post_body = self.rfile.read(content_len)
        post_data = self.rfile.read(content_length)# <--- Gets the data itself
        # files = {'file': ('report.xls', open('report.txt', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
        # post_data2 = self.rfile.read(b'files')
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                     str(self.path), str(self.headers), post_data.decode('utf-8'))

        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

    def do_PUT(self):
        self.do_POST()



    #def do_DELETE(self):



def run(server_class=HTTPServer, handler_class=S, port=PORT):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

# try:
#     httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
#     httpd.serve_forever()
# except Exception:
#     httpd.shutdown()

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

# def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
#     server_address = ('', 9500)
#     httpd = server_class(server_address, handler_class)
#     httpd.serve_forever()
