import file_handler as fh
from functools import reduce

# ============== FUNCTIONS ===============


def get_valid_marks():

    while True:

        try:
            marks = int(input("Enter student marks : "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100...")

        except ValueError:
            print("Please enter a valid number")


def show_students(students):

    print("========= All Students =========")
    print()

    if not students:
        print("No students available...")
        return
    
    for student in students:
        print(f"{student['name']} : {student['marks']}")


def add_student(students):

    student_name = input("Enter student name : ")

    for student in students:

        if student['name'].lower() == student_name.lower():
            print("Student already exists...")
            return

    student_marks = get_valid_marks()

    students.append({
        "name": student_name,
        "marks": student_marks
    })

    fh.save_students(students)

    print("Student added successfully")

def search_student(students):
    student_name = input("Enter student name : ")

    for student in students:
        if student['name'].lower() == student_name.lower():
            return student            
    return None


def update_marks(students):
    student_name = input("Enter student name : ")

    for student in students:
        if student_name.lower() == student['name'].lower():

            student_new_marks = get_valid_marks()

            student['marks'] = student_new_marks

            fh.save_students(students)

            return student

    return None


def delete_student(students):
    student_name = input("Enter student name : ")

    for student in students:
        if student['name'].lower() == student_name.lower():

            students.remove(student)

            fh.save_students(students)

            print("Student deleted successfully")
            break

    else:
        print("Student not found")


def show_statistics(students):

    if not students:
        print("No students available...")
        return
    
    # For total students
    total_students = len(students)

    # For total marks
    total_marks = reduce(
        lambda total, student: total + student['marks'],
        students,
        0
    )

    # For average marks
    average_marks = total_marks / len(students)
    
    # For find topper student
    highest = students[0]

    for student in students:
        if student['marks'] > highest['marks']:
            highest = student

    # For find loser student
    lowest = students[0]

    for student in students:
        if student['marks'] < lowest['marks']:
            lowest = student

    # Students report
    print("====== Student Statistics ======")
    print()

    print(f"Total Students  : {total_students}")
    print(f"Total Marks     : {total_marks}")
    print(f"Average Marks   : {round(average_marks, 2)}")
    print(f"Highest Marks   : {highest['name']} : {highest['marks']}")
    print(f"Lowest Marks    : {lowest['name']} : {lowest['marks']}")


def show_above_average_students(students):

    if not students:
        print("No students available...")
        return

    total_marks = sum(student['marks'] for student in students)

    average_marks = total_marks / len(students)

    print("===== Above Average Students =====")
    print()

    above_average = list(
        filter(
            lambda student: student['marks'] > average_marks,
            students
        )
    )

    for student in above_average:
            print(f"{student['name']} : {student['marks']}")
            

def show_pass_students(students):

    passed_students = filter(
        lambda student: student['marks'] >= 70,
        students
    )
    
    print("========= Pass Students =========")
    print()

    for student in passed_students:
        print(f"{student['name']} : {student['marks']}")


def show_fail_students(students):

    if not students:
        print("No students available...")
        return

    print("========== Fail Students ===========")
    print()

    for student in students:
        if student['marks'] < 70:
            print(f"{student['name']} : {student['marks']}")


def count_pass_students(students):
    pass_students = 0

    for student in students:
        if student['marks'] >= 70:
            pass_students += 1

    return pass_students


def count_fail_students(students):
    fail_students = 0

    for student in students:
        if student['marks'] < 70:
            fail_students += 1

    return fail_students


def get_students_by_grade(students):
    for student in students:
        if student['marks'] >= 90:
            print(f"{student['name']} : Excellent")
        elif student['marks'] >= 80:
            print(f"{student['name']} : Very Good")
        elif student['marks'] >= 70:
            print(f"{student['name']} : Good")
        else:
            print(f"{student['name']} : Needs Improvement")

