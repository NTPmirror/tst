from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        return

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'test')

print("Сервер запущен на порту 8081. Жду запросов...")
try:
    HTTPServer(('127.0.0.1', 8081), SimpleHandler).serve_forever()
except KeyboardInterrupt:
    print("\nСервер остановлен.
    ")
