import json
import os

def load_students():
    file_path = os.path.join(os.path.dirname(__file__), "students.json")
    with open(file_path, "r") as file:
        return json.load(file)
    

def save_students(students):
    file_path = os.path.join(os.path.dirname(__file__), "students.json")
    with open(file_path, "w") as file:
        json.dump(students, file, indent=4)


