import time
import BaseHTTPServer
import SimpleHTTPServer
import urlparse
import json
import model
import storage


HOST_NAME = 'localhost'
PORT_NUMBER = 8080

# Please don't do this in real life
storage = storage.Storage()

def create_event(request):
    event = model.event_from_json(request)
    storage.insert_or_update(event)
    return 200, model.event_to_json(event)

def update_event(request):
    event_id = storage.insert_or_update(model.event_to_json(event))
    return 200, event_id

def delete_event(request):
    storage.remove(model.event_to_json(event))
    return 200, ''

def retrieve_event(request):
    return 200, storage.get(request['id'])

def retrieve_all_events(request):
    events = storage.get_all()
    print events
    return 200, json.dumps(events)

API_ENDPOINTS = {
    'POST': {
        '/api/create_event': create_event,
        '/api/update_event': update_event,
        '/api/delete_event': delete_event
    },
    'GET': {
        '/api/retrieve_event': retrieve_event,
        '/api/retrieve_all_events': retrieve_all_events
    },
}

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def handle_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

    def get_api_path(self, path):
        if not str(path).startswith('/api/'):
            return None
        if '?' in path:
            path = path[:path.find('?')]
        return path

    def get_endpoint_handler(self, method, path):
        endpoints =  API_ENDPOINTS.get(method, None)
        if not endpoints:
            return None
        return endpoints.get(path, None)

    def do_GET(self):
        print 'GET request coming in'
        self.handle_headers()
        path = self.get_api_path(self.path)
        method = self.command
        endpoint_handler = self.get_endpoint_handler(method, path)
        if not endpoint_handler:
            print 'Could not find %s' % (path)
            self.send_response(404)
            return
        status, resp = endpoint_handler(self.get_url_paramters(path))
        self.send_response(status)
        if status == 200:
            self.wfile.write(resp)
        return

    def do_POST(self):
        print 'POST request coming in'
        data_string = self.rfile.read(int(self.headers['Content-Length']))
        self.handle_headers()
        path = self.get_api_path(self.path)
        method = self.command
        print path
        endpoint_handler = self.get_endpoint_handler(method, path)
        if not endpoint_handler:
            print 'Could not find %s' % (path)
            self.send_response(404)
            return
        print data_string
        status, resp = endpoint_handler(json.loads(data_string))
        self.send_response(status)
        if status == 200:
            self.wfile.write(resp)
        return

    def get_url_paramters(self, path):
        params = urlparse.parse_qs(urlparse.urlparse(path).query)
        return params


def run():
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), ServerHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        passc
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)

run()
