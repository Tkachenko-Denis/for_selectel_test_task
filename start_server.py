from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler

server_address = ("", 9000)
server = HTTPServer(server_address, CGIHTTPRequestHandler)
server.serve_forever()
