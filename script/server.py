from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        user_agent = self.headers.get('User-Agent')
        with open('user_agents.txt', 'a') as f:
            f.write(user_agent + '\n')
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'User-Agent capturado!')
        logging.info(f'User-Agent: {user_agent}')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Servidor HTTP corriendo en puerto 8080...')
    httpd.serve_forever()