from flask import Flask, request
import flask
from waitress import serve
import pyperclip

from utilities import *


app = Flask(__name__)
# app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>MicroDroid Interface running<h1>"


@app.route('/copytopc', methods=['POST'])
def copy():
    data: flask.request = request.get_json()
    if data['from'] == 'OnePlus Nord N10 5G':
        data['from'] = 'OnePlus N10'
    
    pyperclip.copy(data['content'])
    show_notification(f"Copied from {data['from']}", data['content'])

    print(f"[{data['from']}] Copy: {data['content']}")

    return 'SUCCESS'



print('[STARTED] Running on http://192.168.31.3:5000')
print('[COPY-TO-PC] Running on http://192.168.31.3:5000/copytopc')

# app.run(host='0.0.0.0', port=5000)
serve(app, host='0.0.0.0', port=5000)

