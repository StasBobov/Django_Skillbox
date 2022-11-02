from http.server import HTTPServer, BaseHTTPRequestHandler

# запускаем сервер на нашей машине (либо 127.0.0.1)
APP_HOST = 'localhost'
# порт на котором будет работать сервер
APP_PORT = 8000


class SimpleGetHandler(BaseHTTPRequestHandler):
    # какие заголовки должны быть в запросе
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

    # преобразовываем сообщение в html код
    def _html(self, messages):
        content = ('<html>'
                   '<body>'
                   f'<h1>{messages[0]}</h1>'
                   f'<h2>{messages[1]}</h2>'
                   '</body>'
                   '</html>')
        return content.encode('utf-8')


    def do_GET(self):
        self._set_headers()
        messages = []
        messages.append('Hello, SIDNEY!')
        messages.append('Do you like a scary movies?')
        # отправляем контент клиенту
        self.wfile.write(self._html(messages))


# инициализация сервера
def run_server(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = (APP_HOST, APP_PORT)
    httpd = server_class(server_address, handler_class)
    # сервер нужно хранить вечно пока сами не выключим (или выпадет ошибка)
    httpd.serve_forever()


if __name__ == '__main__':
    run_server(handler_class=SimpleGetHandler)