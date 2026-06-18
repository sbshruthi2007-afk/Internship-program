import csv
import json

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "score": self.score
        }

students = [
    Student("Shruthi", 18, 90),
    Student("Rahul", 19, 85),
    Student("Anu", 18, 95)
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "age", "score"])

    for student in students:
        writer.writerow([student.name, student.age, student.score])

loaded_students = []

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        loaded_students.append({
            "name": row[0],
            "age": int(row[1]),
            "score": int(row[2])
        })

with open("students.json", "w") as file:
    json.dump(loaded_students, file, indent=4)

with open("students.json", "r") as file:
    data = json.load(file)

print(data)