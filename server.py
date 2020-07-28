import json
import os
from flask import Flask, Response

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STUDENT_FILE = os.path.join(BASE_DIR, 'students.json')


def select_students():
    content = ""
    file_text = open(STUDENT_FILE, "r", encoding='utf-8').readlines()
    for line in file_text:
        content += line
    return content


@app.route("/students")
def get_students():
    return Response(select_students(),
                    headers={"Content-Type": "application/json"},
                    mimetype="application/json",
                    status=200)


@app.route("/students/<id>")
def get_students_by_id(id):
    students = json.loads(select_students())
    result = None
    for student in students:
        if student["id"] == int(id):
            result = student
            break

    return Response(json.dumps(result,ensure_ascii=False),
                    headers={"Content-Type": "application/json"},
                    mimetype="application/json",
                    status=200)


app.run(host="127.0.0.1", debug=True, port=5000)
