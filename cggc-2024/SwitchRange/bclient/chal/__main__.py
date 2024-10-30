#!/usr/bin/env python3

import json
import socket

dbport = 8787

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("0.0.0.0", dbport))

users = {}

def getuser(username):
    result = None
    if username in users:
        result = users[username]
    return result

def setuser(user):
    if 'username' not in user or type(user['username']) != str or 'password' not in user or type(user['password']) != str or 'admin' not in user or type(user['admin']) != bool:
        return False
    users[user['username']] = user
    return True

while True:
    try:
        data, address = sock.recvfrom(65535)
        data = json.loads(data.decode('utf-8'))
        result = None
        if data['command'] == 'get' and type(data['data']) == str:
            result = getuser(data['data'])
        elif data['command'] == 'set' and type(data['data']) == dict:
            result = setuser(data['data'])
        sock.sendto(json.dumps(result).encode('utf-8'), address)
    except:
        pass



