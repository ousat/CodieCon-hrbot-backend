import os

from flask import Flask, jsonify, request, redirect, url_for, send_file
from werkzeug import secure_filename
from database import save_profile, get_last_profile

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


# @app.route('/resume')
# def resume():
#     # with open('/home/user/codiecon/hrbot/Resume_1.pdf', 'rb') as static_file:
#     return send_file('/home/user/codiecon/hrbot/Resume_1.pdf')

@app.route('/resume/<fid>')
def resume_id(fid):
    file_name = '/home/user/codiecon/hrbot/pdf/'+str(fid)+'.pdf'
    return send_file(file_name)


@app.route('/profile-details', methods=['POST'])
def profile_form():
    fn = request.form["first_name"]
    mn = request.form["middle_name"] if "middle_name" in request.form else None
    ln = request.form["last_name"]
    email = request.form["email"]
    dob = request.form["dob"]
    addrs = request.form["addrs"]
    contact = request.form["contact"]
    resume_file = request.files['resume']
    exprnc = request.form['exp']
    skills = request.form['skills']
    # print(idno)
    last_val = get_last_profile()
    print(last_val)
    file_name = "pdf/" + str(last_val+1) + ".pdf"
    resume_file.save(file_name)
    status = save_profile(fn, ln, mn, dob, addrs, email, contact, exprnc, skills, file_name)
    if not type(status) == dict:
        return jsonify({"status": False})
    return jsonify(status)

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    # print(f)
    f.save(secure_filename(f.filename))
    # print(f.filename)
    return jsonify({"filename": f.filename})


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
