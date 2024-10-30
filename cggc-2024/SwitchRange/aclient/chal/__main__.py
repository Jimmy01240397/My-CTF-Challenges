#!/usr/bin/env python3

from flask import Flask,request,redirect,Response,render_template,session,make_response
import json
import os
import socket
from dotenv import load_dotenv

load_dotenv()

port = int(os.getenv("PORT", 5000))

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

dbhost = '192.168.110.1'
dbport = 8787

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.settimeout(0.1)

def getuser(username):
    try:
        sock.sendto(json.dumps({'command': 'get', 'data': username}).encode('utf-8'), (dbhost, dbport))
        data, address = sock.recvfrom(65535)
        user = json.loads(data.decode('utf-8'))
        return user
    except:
        return None

def setuser(user):
    try:
        sock.sendto(json.dumps({'command': 'set', 'data': user}).encode('utf-8'), (dbhost, dbport))
        data, address = sock.recvfrom(65535)
        state = json.loads(data.decode('utf-8'))
        return state
    except:
        return False

@app.route('/',methods=['GET'])
def root():
    user = None
    if 'username' in session:
        user = getuser(session['username'])
        if user['admin']:
            tmpuser = dict(user)
            tmpuser['admin'] = False
            setuser(tmpuser)
    return render_template('index.html', user=user, flag=os.getenv("FLAG"))

@app.route('/account', methods=['POST'])
def account():
    if 'user' not in request.form or type(request.form['user']) != str or 'pass' not in request.form or type(request.form['pass']) != str:
        return redirect("/", code=302)
    user = getuser(request.form['user'])
    if user == None:
        user = {"username": request.form['user'], "password": request.form['pass'], "admin": False}
        setuser(user)
    if user["username"] == request.form['user'] and user["password"] == request.form['pass']:
        session['username'] = user['username']
    return redirect("/", code=302)

@app.route('/source', methods=['GET'])
def source():
    data = '__main__.py:'
    with open('__main__.py', 'r') as f:
        data += '\n\n' + f.read() + '\n\n'
    data += 'index.html:'
    with open('templates/index.html', 'r') as f:
        data += '\n\n' + f.read() + '\n\n'
    r = make_response(data, 200)
    r.mimetype = "text/plain"
    return r

if __name__ == "__main__":
    app.run(host="::", port=port)
