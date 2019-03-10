import os
import json
from flask import Flask, jsonify, request, redirect, url_for, send_file
from werkzeug import secure_filename
from database import save_profile, get_last_profile, validate, get_file_name, select_questions, get_answer
from analytics import process_pdf, score_calculation

# from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'abcdef'
# socketio = SocketIO(app)

HOST = "0.0.0.0"
PORT = 8787

# FILE_ROOT = "/home/user/codiecon/hrbot/"

@app.route('/')
def index():
    return jsonify({})


@app.route('/questions', methods=['POST'])
def rqsn():
    values = request.get_json()
    resume_file = get_file_name(values["user_id"])
    # print(process_pdf(resume_file))
    # return jsonify([{"question": "What is dictionary in Python?", "category": "python", "user_id": 1},
    #                 {"question": "Difference between overloading and overriding?", "category": "OOPS", "user_id": 1},
    #                 {"question": "What are Pseudo-elements?", "category": "CSS", "user_id": 1},
    #                 {"question": "What is this keyword in JavaScript?", "category": "JavaScript", "user_id": 1},
    #                 {"question": " What is meant by an Abstract class?", "category": "Java", "user_id": 1}])
    # pdf_keywords = process_pdf(resume_file)
    user_questions = select_questions(process_pdf(resume_file))
    for user_question in user_questions:
        user_question["user_id"] = values["user_id"]
    return jsonify(user_questions)


@app.route('/submit', methods=['POST'])
def submit():
    answer_values = request.get_json()
    total_score = 0
    for entry in answer_values:
        answer = get_answer(entry["question"])
        score = score_calculation(answer, entry["answer"])
        total_score = total_score + score

    return jsonify({"response": "OK", "scores": total_score})


@app.route('/login', methods=['POST'])
def login():
    values = request.get_json()
    return jsonify(validate(values["email"], values["password"]))


@app.route('/profile-details', methods=['POST'])
def profile_form():
    # print(request.form)
    fn = request.form["first_name"]
    pwd = request.form["password"]
    email = request.form["email"]
    resume_file = request.files['resume']
    # print(idno)
    last_val = get_last_profile()
    # print(last_val)
    file_name = "/home/user/codiecon/hrbot/pdf/" + str(last_val+1) + ".pdf"
    resume_file.save(file_name)
    status = save_profile(fn, email, pwd, file_name)
    if not type(status) == dict:
        return jsonify({"status": False})
    return redirect("http://10.177.7.104:8080/login")


@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    # print(f)
    f.save(secure_filename(f.filename))
    # print(f.filename)
    return jsonify({"filename": f.filename})


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
    # socketio.run(app, host='0.0.0.0', port=8787)


# @app.route('/resume')
# def resume():
#     # with open('/home/user/codiecon/hrbot/Resume_1.pdf', 'rb') as static_file:
#     return send_file('/home/user/codiecon/hrbot/Resume_1.pdf')

# @socketio.on('message')
# def handle_message(message):
#     send(message)
#
# @socketio.on('json')
# def handle_json(json):
#     send(json, json=True)
#
# @socketio.on('question')
# def handle_my_custom_event(json):
#     emit('my response', json)
#
# @app.route('/resume/<fid>')
# def resume_id(fid):
#     file_name = '/home/user/codiecon/hrbot/pdf/'+str(fid)+'.pdf'
#     return send_file(file_name)
