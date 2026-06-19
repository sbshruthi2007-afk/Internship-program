from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('add_student.html')


@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    age = request.form['age']

    file_exists = os.path.isfile('students.csv')

    with open('students.csv', 'a', newline='') as file:
        writer = csv.writer(file)

        # optional: add header only first time
        if not file_exists:
            writer.writerow(['Name', 'Age'])

        writer.writerow([name, age])

    return "Student added successfully!"


if __name__ == '__main__':
    app.run(debug=True)