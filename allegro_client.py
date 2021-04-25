# -*- coding: utf-8 -*-
"""
@author: Michał Worsowicz
"""

import requests
from sys import argv

"""
Client application which sends the GET requests to the server established at
host:port and represents the returned data in legible form.
    
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

user = input("Input GitHub username or click enter to finish: ")

while user != "":
    request = requests.get('http://' + host + ':' + str(port), params={'user':str(user)})
    
    if request.status_code == 404:
        user = input("No such user! Input another GitHub username or click enter to finish: ")
        continue
    elif request.status_code != 200:
        user = input("Error " + str(request.status_code) + "! Input another GitHub username or click enter to finish: ")
    
    repos = request.json()
    
    print("\nUser: " + str(user))
    print("\nRepositories: ")
    
    if len(repos['repositories']) == 0:
            print("User have no repositories")
    else:   
        for i,r in enumerate(repos['repositories']):
            print(str(i+1) + ".\tRepository name: " + str(r['name']) 
                  + "\n\tNumber of stars: " + str(r['stars_no']))
                
    print("\nTotal number of stars: " + str(repos['total_stars']))
    user = input("\nInput another GitHub username or click enter to finish: ")
