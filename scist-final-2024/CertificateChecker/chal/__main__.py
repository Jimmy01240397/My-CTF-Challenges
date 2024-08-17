#!/usr/bin/env python3

from flask import Flask,request,redirect,Response,render_template,session
import json
import hashlib
import os
import urllib.parse
import io
from asn1crypto import pem
from certvalidator import CertificateValidator, ValidationContext
from dotenv import load_dotenv

load_dotenv()

port = 39999

users = {}

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

def sendverifyurltoadminemail(verifyurl):
    # TODO
    pass


@app.route('/',methods=['GET'])
def root():
    valid = 'username' in session and session['username'] in users and users[session['username']]['valid']
    if valid:
        del users[session['username']]
        del session['username']
    certvalid = session['certvalid'] if 'certvalid' in session else ''
    userstatus = session['userstatus'] if 'userstatus' in session else ''
    session['certvalid'] = ''
    session['userstatus'] = ''
    return render_template('index.html', valid=valid, certvalid=certvalid, userstatus=userstatus, flag=os.getenv("FLAG"))

@app.route('/account', methods=['POST'])
def account():
    if request.form['action'] == 'login':
        session['userstatus'] = login()
    elif request.form['action'] == 'signup':
        session['userstatus'] = signup()
    return redirect("/", code=301)

def login():
    if request.form['user'] not in users:
        return 'user not exist'
    userdata = users[request.form['user']]
    if request.form['user'] == userdata['user'] and request.form['pass'] == userdata['pass']:
        if not userdata['valid']:
            return 'user not valid'
        session['username'] = userdata['user']
    else:
        return 'password not correct'
    return ''

def signup():
    if request.form['user'] in users:
        return 'user exist'
    users[request.form['user']] = {"user": request.form['user'], "pass": request.form['pass'], "valid": False}
    md5 = hashlib.md5()
    md5.update(request.form['user'].encode())
    md5.update(request.form['pass'].encode())
    verifyurl = urllib.parse.urlunparse(["http", f"localhost:{port}", "verifyaccount", "", urllib.parse.urlencode({"user": request.form['user'], "verify": md5.hexdigest()}), ''])
    sendverifyurltoadminemail(verifyurl)
    return 'signup success, wait for admin verify'

@app.route('/verifyaccount',methods=['GET','POST'])
def verifyaccount():
    ip = request.environ['REMOTE_ADDR']
    if ip != '127.0.0.1' and ip != '::1' and ip != '::ffff:127.0.0.1':
        return 'Not Found', 404
    user = request.args['user']
    verify = request.args['verify']
    md5 = hashlib.md5()
    md5.update(users[user]['user'].encode())
    md5.update(users[user]['pass'].encode())
    users[user]['valid'] = verify == md5.hexdigest()
    return str(users[user]['valid'])

@app.route('/certvalid', methods=['POST'])
def certvalid():
    files = {}
    for nowfile in request.files:
        files[nowfile] = io.BytesIO()
        request.files[nowfile].save(files[nowfile])
        files[nowfile].seek(0)

    extra_trust_roots = []
    if 'trustanchor' in files:
        trustanchor = files['trustanchor'].read()
        if len(trustanchor) > 0:
            extra_trust_roots.append(trustanchor)

    end_entity_cert = None
    intermediates = []
    for type_name, headers, der_bytes in pem.unarmor(files['certificate'].read(), multiple=True):
        if end_entity_cert is None:
            end_entity_cert = der_bytes
        else:
            intermediates.append(der_bytes)

    context = ValidationContext(allow_fetching=True, extra_trust_roots=extra_trust_roots)
    validator = CertificateValidator(end_entity_cert, intermediates, validation_context=context)

    try:
        validator.validate_usage(set(['digital_signature']))
        session['certvalid'] = 'Valid'
    except Exception as e:
        session['certvalid'] = str(e)
    return redirect("/", code=301)
        

if __name__ == "__main__":
    app.run(host="::", port=port, threaded=True)
