from flask import Flask, request
import flask
from waitress import serve
import pyperclip
from threading import Thread

from utilities import *


app = Flask(__name__)
# app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>MicroDroid Interface running<h1>"


@app.route('/copytopc', methods=['POST'])
def copy_to_pc():
    data: flask.request = request.get_json()
    # if data['from'] == 'OnePlus Nord N10 5G':
    #     data['from'] = 'OnePlus N10'
    
    pyperclip.copy(data['content'])

    action_thread = Thread(target=action, args=(data, ))
    action_thread.start()

    return 'SUCCESS'


@app.route('/copyfrompc', methods=['GET'])
def copy_from_pc():
    clipboard = pyperclip.paste()

    return clipboard


print('[STARTED] Running on http://192.168.31.3:5000')
print('[COPY-TO-PC] Running on http://192.168.31.3:5000/copytopc')
print('[COPY-FROM-PC] Running on http://192.168.31.3:5000/copyfrompc')


# app.run(host='0.0.0.0', port=5000)
serve(app, host='0.0.0.0', port=5000)

