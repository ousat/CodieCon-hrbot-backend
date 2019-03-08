import os

from flask import Flask, jsonify, request, redirect, url_for, send_file
from werkzeug import secure_filename
from database import save_profile

app = Flask(__name__)

UPLOAD_FOLDER = '/home/user/codiecon/hrbot'
ALLOWED_EXTENSIONS = set(['pdf'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS

HOST = "0.0.0.0"
PORT = 8787

@app.route('/')
def index():
    return jsonify({})

@app.route('/rqsn')
def rqsn():
    return jsonify({"question": "what are some of the most prominent features of Python?"})


@app.route('/resume')
def resume():
    # with open('/home/user/codiecon/hrbot/Resume_1.pdf', 'rb') as static_file:
    return send_file('/home/user/codiecon/hrbot/Resume_1.pdf')


@app.route('/profile-details', methods=['POST'])
def profile_form():
    idno = request.form["id_value"]
    idty = request.form["id_type"]
    name = request.form["name"]
    email = request.form["email"]
    # print(idno)
    status = save_profile(idno, idty, name, email)
    if not type(status) == dict:
        return jsonify({"status": False})
    return jsonify(status)

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    print(f)
    f.save(secure_filename(f.filename))
    print(f.filename)
    return jsonify({"filename": f.filename})


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
