import student_functions as sf
import file_handler as fh

students = fh.load_students()

# =============== MENU =================

while True:

    print("\n===== Student Management System =====")
    print("1. Show all students")
    print("2. Add Student")
    print("3. Search student")
    print("4. Update marks")
    print("5. Delete student")
    print("6. Show Statistics")
    print("7. Show Above Average Students")
    print("8. Show Pass Students")
    print("9. Show Fail Students")
    print("10. Count Pass Students")
    print("11. Count Fail Students")
    print("12. Get Students by Grade")
    print("13. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":

        sf.show_students(students)

    elif choice == "2":

        sf.add_student(students)

    elif choice == "3":

        student = sf.search_student(students)

        if student:
            print("=========== Student Found ===========")
            print()

            print(f"Name   : {student['name']}")
            print(f"Marks  : {student['marks']}")
        else:
            print("Student not found")

    elif choice == "4":

        student = sf.update_marks(students)

        if student:
            print("Marks updated successfully")
            print(f"{student['name']} : {student['marks']}")
        else:
            print("Student not found")

    elif choice == "5":

        sf.delete_student(students)

    elif choice == "6":

        sf.show_statistics(students)

    elif choice == "7":

        sf.show_above_average_students(students)

    elif choice == "8":

        sf.show_pass_students(students)

    elif choice == "9":

        sf.show_fail_students(students)

    elif choice == "10":

        print(f"Pass Students : {sf.count_pass_students(students)}")

    elif choice == "11":

        print(f"Fail Students : {sf.count_fail_students(students)}")

    elif choice == "12":

        sf.get_students_by_grade(students)

    elif choice == "13":

        print("Exiting Program...")
        break

    else:
        print("Please enter from the numbers given above...")

    print()
    print("=======================================")
        
