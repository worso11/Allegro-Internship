# -*- coding: utf-8 -*-
"""
@author: Michał Worsowicz
"""

import requests
from http.server import HTTPServer, BaseHTTPRequestHandler
from sys import argv
from urllib.parse import urlparse
import json


class Server_Application(BaseHTTPRequestHandler):
    """
    Class to represent a server application which lists repositories (with stars)
    and returns the total number of stars for a given user.
    
    Methods:
        do_GET() -> parses username from an URL, sends a GET request to GitHub API,
        extracts data needed and returns them in a form of JSON file.
        In case of status code different to 200 (OK), it sends response with
        a given code.
    """
    
    def do_GET(self):
        url_query = urlparse(self.path).query
        query_components = dict(query.split("=") for query in url_query.split("&"))
        user = query_components["user"]        
        
        request = requests.get('https://api.github.com/users/' + user + '/repos')
        
        if (request.status_code != 200):
            self.send_response(request.status_code)
            self.end_headers()
            return
        
        repos = request.json()
        stars_count = 0;
        
        info = {}
        info['repositories'] = []
        
        for i,r in enumerate(repos):
            info['repositories'].append({
                'name': r['name'],
                'stars_no' : r['stargazers_count']
                })
            stars_count += r['stargazers_count']
        
        info['total_stars'] = stars_count
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(json.dumps(info), 'utf-8'))


if __name__ == "__main__":
    """
    Main function, establishes HTTPServer on a given host:port and handles requests
    
    Variables:
        host -> name of the host, localhost by default,
        port -> number of port, 80 by default
        
    Those values can be changed by passing argument in a form host:port
    """
    
    host = 'localhost'
    port = 80
    
    if len(argv) > 1:
        arg = argv[1].split(':')
        host = arg[0]
        port = int(arg[1])
    
    print('Listening on http://' + str(host) + ':' + str(port) + '\n')
    
    server = HTTPServer((host, port), Server_Application)
    server.serve_forever()

        
