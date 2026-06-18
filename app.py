from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "Shruthi", "age": 18},
    {"id": 2, "name": "Rahul", "age": 20}
]

@app.route("/")
def home():
    return "<h1>Welcome to Flask</h1>"

@app.route("/students")
def get_students():
    return jsonify(students)

if __name__ == "__main__":
    app.run(debug=True)