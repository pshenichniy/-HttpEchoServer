import logging
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 9000

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def payload(self):
        payload_size = int(self.headers['Content-Length'])
        payload = self.rfile.read(payload_size).decode()
        return payload

    def do_GET(self):
        payload = self.payload()
        self._set_headers()
        get_data = self.wfile.write("GET request for {} with payload: {}".format(self.path, payload).encode('utf-8'))
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                     str(self.path), str(self.headers), get_data)


    def do_POST(self):
        payload = self.payload()
        self._set_headers()
        post_data = self.wfile.write("POST: {}".format(payload).encode('utf-8'))
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
        str(self.path), str(self.headers), post_data)

    def do_PUT(self):
        payload = self.payload()
        self._set_headers()
        put_data = self.wfile.write("PUT request for {}".format(payload).encode('utf-8'))
        logging.info("PUT request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers),put_data)

    def do_DELETE(self):
        payload = self.payload()
        self._set_headers()
        del_data = self.wfile.write("DELETE request for {}".format(payload).encode('utf-8'))
        logging.info("DELETE request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers),del_data)




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



if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

