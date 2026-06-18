class Student:
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores  
    def average_score(self):
        return sum(self.scores) / len(self.scores)
    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Scores:", self.scores)
    def add_score(self, score):
        self.scores.append(score)
s1 = Student("Shruthi", 18, [85, 90, 88])
s1.display_details()
print("Average Score:", s1.average_score())
s1.add_score(95)
print("Updated Scores:", s1.scores)
print("New Average:", s1.average_score())     
