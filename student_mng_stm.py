student_grades = {}

def add_student(name,grade):
    student_grades[name] = grade
    print(f"Added {name} with grade {grade}")

def update_student(name,grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name} is updated with grade {grade}")
    else:
        print(f"{name} is not found...")

def del_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} is deleted")
    else:
        print(f"{name} is not found")

def disply_all_students():
    if student_grades:
        for name,grade in student_grades.items():
            print(f"{name} : {grade}")
    else:
        print("no students found")

def main():
    while True:
        print("\n============student grade mng system============")
        print("1. Add student")
        print("2. Update student")
        print("3. Delete student")
        print("4. View student")
        print("5. Exit")

        choice = int(input("enter your choice = "))
        if choice == 1:
            name = input("enter your name : ")
            grade = input("enter your grade : ")
            add_student(name,grade)
        elif choice == 2:
            name = input("enter your name : ")
            grade = input("enter your grade : ")
            update_student(name,grade)
        elif choice == 3:
            name = input("enter your name : ")
            del_student(name)
        elif choice == 4:
            disply_all_students()
        elif choice == 5:
            print("closing the programme")
            break
        else:
            print("Invalid name!")

if __name__ == "__main__":
    main()