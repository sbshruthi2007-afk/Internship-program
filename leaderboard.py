import csv

students = []

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        students.append({
            "name": row[0],
            "age": int(row[1]),
            "score": int(row[2])
        })

sorted_students = sorted(
    students,
    key=lambda student: student["score"],
    reverse=True
)

average = sum(student["score"] for student in students) / len(students)

print("LEADERBOARD")
print("-" * 30)

for rank, student in enumerate(sorted_students, start=1):
    print(f"{rank}. {student['name']} - {student['score']}")

print("\nTop 3 Students")
for student in sorted_students[:3]:
    print(student["name"], "-", student["score"])

print("\nBottom 3 Students")
for student in sorted_students[-3:]:
    print(student["name"], "-", student["score"])

print("\nAverage Score:", average)