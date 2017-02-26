# This program starts up a web server to run the CGI scripts in our "cgi-bin"
# sub-directory.

import BaseHTTPServer
import CGIHTTPServer

address = ('', 8000)
handler = CGIHTTPServer.CGIHTTPRequestHandler
server = BaseHTTPServer.HTTPServer(address, handler)
server.serve_forever()

