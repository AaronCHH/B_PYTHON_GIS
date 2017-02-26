import BaseHTTPServer
import CGIHTTPServer

address = ('', 8000)
handler = CGIHTTPServer.CGIHTTPRequestHandler
handler.cgi_directories=["/cgi-bin", "elsewhere"]
server = BaseHTTPServer.HTTPServer(address, handler)
server.serve_forever()

