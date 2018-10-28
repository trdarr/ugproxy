from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

from ugproxy import ultimateguitar


class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = urlparse(self.path)

        if path.path.startswith('/tab'):
            base_url = 'https://tabs.ultimate-guitar.com'
            metadata, tab = ultimateguitar.get_tab(base_url + self.path)
            title, artist = metadata['song_name'], metadata['artist_name']

            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()

            self.wfile.write(tab.encode('utf-8'))

        else:
            self.send_response(404)
            self.end_headers()

def create_server(address):
    return HTTPServer(address, HTTPRequestHandler)
