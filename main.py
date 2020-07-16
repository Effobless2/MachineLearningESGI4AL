from http.server import BaseHTTPRequestHandler, HTTPServer
host_name = "localhost"
host_port = 8080

from ml import hello

algoFileName1 = 'linear'
algoFileName2 = 'conv'
algoFileName3 = 'none'
algoFileName4 = 'none'

def getModelName(input):
    result = algoFileName1
    if input == '' :
        result = algoFileName1
    elif input == '1' :
        result = algoFileName1
    elif input == '2' :
        result = algoFileName2
    elif input == '3' :
        result = algoFileName3
    else :
        result = algoFileName4
    return result

class MyServer(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'plain/text')
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        image = self.rfile.read(content_length)
        algoFile = getModelName(self.path[1:])

        result = hello(image, algoFile)

        self.do_HEAD()
        self.wfile.write(result.encode('utf-8'))

    def do_GET(self):
        self.do_HEAD()
        self.wfile.write('OK'.encode('utf-8'))

if __name__ == '__main__':
    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Running server on %s:%s" % (host_name, host_port))
    http_server.serve_forever()