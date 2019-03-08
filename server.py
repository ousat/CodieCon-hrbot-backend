from flask import Flask, jsonify, request, redirect, url_for
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
def hello():
    return jsonify({"question": "what are some of the most prominent features of Python?"})

@app.route('/profile-details', methods=['POST'])
def profile_form():
    idno = request.form["id_value"]
    idty = request.form["id_type"]
    name = request.form["name"]
    email = request.form["email"]
    status =  save_profile(idno, idty, name, email)
    return jsonify({"status": status})

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_files = request.files.getlist("file[]")
    filenames = []
    for file in uploaded_files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filenames.append(filename)
            return jsonify({"upload": True, "filename": filename})
        else:
            return jsonify({"upload": False, "message": "invalid file"})

    return jsonify({})


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
