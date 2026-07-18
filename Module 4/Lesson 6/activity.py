def add_student(gradebook, student_name):
    if student_name in gradebook:
        print(f"Student '{student_name}' already exists.")
        return False
    gradebook[student_name] = []
    print(f"Added student '{student_name}'.")
    return True


def add_grade(gradebook, student_name, grade):
    if student_name not in gradebook:
        print(f"Student '{student_name}' not found.")
        return False
    try:
        grade_value = float(grade)
    except ValueError:
        print("Grade must be a number.")
        return False
    if grade_value < 0 or grade_value > 100:
        print("Grade must be between 0 and 100.")
        return False
    gradebook[student_name].append(grade_value)
    print(f"Added grade {grade_value} for '{student_name}'.")
    return True


def average_grade(grades):
    if not grades:
        return None
    return sum(grades) / len(grades)


def print_gradebook(gradebook):
    if not gradebook:
        print("Grade book is empty.")
        return
    print("\nGrade Book:")
    for student, grades in gradebook.items():
        avg = average_grade(grades)
        grades_text = ", ".join(f"{g:.1f}" for g in grades) if grades else "No grades"
        avg_text = f"{avg:.1f}" if avg is not None else "N/A"
        print(f"- {student}: Grades [{grades_text}] | Average: {avg_text}")
    print()


def main():
    gradebook = {}
    while True:
        print("\nStudent Grade Book")
        print("1. Add student")
        print("2. Add grade")
        print("3. Show grade book")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Enter student name: ").strip()
            if name:
                add_student(gradebook, name)
        elif choice == "2":
            name = input("Enter student name: ").strip()
            if not name:
                print("Student name cannot be empty.")
                continue
            grade = input("Enter grade (0-100): ").strip()
            add_grade(gradebook, name, grade)
        elif choice == "3":
            print_gradebook(gradebook)
        elif choice == "4":
            print("Exiting grade book.")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
