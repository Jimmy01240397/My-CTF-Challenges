import sys
import os
import re
from flask import Flask,request,render_template,make_response

allowcommand = ['ping -c 1 -W 1', 'traceroute -n -I -w 3 -A', 'ip route']

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def run():
    command = allowcommand[int(request.form.get('command'))]
    target = request.form.get('target')
    print(command, target, file=sys.stderr)
    if not re.match('^[+-9A-~]*$', target):
        return render_template('index.html', error=True)
    if int(request.form.get('command')) == 2:
        return render_template('index.html', output=os.popen(f'bash -c "{command}"').read())
    return render_template('index.html', output=os.popen(f'bash -c "{command} {target}"').read())

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

if __name__ == '__main__':
    app.run(host='0.0.0.0')
