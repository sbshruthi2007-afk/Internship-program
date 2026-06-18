import logging

logging.basicConfig(
    filename="student.log",
    level=logging.ERROR
)

class ScoreError(Exception):
    pass

class Student:

    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores

        self.validate_name()
        self.validate_scores()

    def validate_name(self):
        if self.name == "":
            raise ValueError("Name cannot be empty")

    def validate_scores(self):
        for score in self.scores:
            if not isinstance(score, (int, float)):
                raise TypeError("Score must be number")

            if score < 0 or score > 100:
                raise ScoreError("Score must be between 0 and 100")

    def average_score(self):
        return sum(self.scores) / len(self.scores)

try:
    s1 = Student("Shruthi", 18, [85, 90, 110])

except ValueError as e:
    print("Value Error:", e)
    logging.error(e)

except TypeError as e:
    print("Type Error:", e)
    logging.error(e)

except ScoreError as e:
    print("Score Error:", e)
    logging.error(e)

else:
    print("Student created successfully")
    print("Average:", s1.average_score())

finally:
    print("Program finished")