# Student Grades Manager

students = {}

while True:
    print("\nOptions:")
    print("1. Add new student")
    print("2. Update student grade")
    print("3. Display all grades")
    print("4. Exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade
        print(f"{name} added with grade {grade}.")

    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print(f"{name}'s grade updated to {grade}.")
        else:
            print("Student not found.")

    elif choice == "3":
        print("\n--- Student Grades ---")
        for name, grade in students.items():
            print(f"{name}: {grade}")

    elif choice == "4":
        break
    else:
        print("Invalid choice.")
