
from genericpath import exists
from http.server import HTTPServer, BaseHTTPRequestHandler
import sqlite3;
 

APP_HOST = '127.0.0.1'
APP_PORT = 666


class SimpleGetHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.end_headers()

    def _html(self, data_page):
        content = ''
        with open("index.html", 'rb') as html_file:
            content = html_file.read().decode('utf-8').format(cards = data_page)
        return content.encode("utf8")

    def _read_file(self, path_file):
        content = ''
        with open(path_file, 'rb') as file:
            content = file.read()
        return content

    def do_GET(self):
        data_url = self.path.split('?')
        path, par = data_url if len(data_url) == 2 else [data_url[0], None]

        if path == "/remove":
            self.send_response(200)
            self.end_headers()

            # Подключение к базе данных (замените "your_database.db" на имя вашей базы данных)
            conn = sqlite3.connect("db.sqlite")
            cursor = conn.cursor()

            sql = "DELETE FROM people WHERE id = ?"

            try:
                cursor.execute(sql, (par,))
                conn.commit()
                print("Данные успешно удалены.")
            except sqlite3.Error as e:
                print("Ошибка при удалении данных:", e)

            conn.close()

            self.wfile.write(f"Объект с ID={par} удален!".encode())
            return

        if path == "/index.html" or path == "/":
            self._set_headers()

            con = sqlite3.connect("db.sqlite")
            cursor = con.cursor()

            data_page = ""
            if par is None:
                cursor.execute("SELECT * FROM people")
            else:
                cursor.execute(f"SELECT * FROM people WHERE name='{par}'")
            for person in cursor.fetchall():
                data_page += '''
            <div id="{id}" class="card">
				<button class="toggle-btn" onclick="removeCard(this)">X</button>
                <a href="/index.html?{name}">
                    <div class="info-user">
                        <img class="image-user" src="user.jpg" style="width: 200px; display: inline"/>
                        <div class="user-data">
                            <p style="font-size: 30px;">Name: {name}</p>
                            <p style="font-size: 20px;">Age: {age}</p>
                        </div>
                    </div>
				    <img class="image-info" src="Honkai-Star-Rail-review.webp" style="width: 100%;;"/>
                </a>
			</div>'''.format(id = person[0], name = person[1], age = person[2])

            self.wfile.write(self._html(data_page))
        else:            
            if exists(path[1:]):
                self._set_headers()
                self.wfile.write(self._read_file(path[1:]))


def run_server(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = (APP_HOST, APP_PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run_server(handler_class=SimpleGetHandler)
