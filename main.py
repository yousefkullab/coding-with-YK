# Mini Project Student Grade Calculator

from utils import (
    add_student,
    calculate_average,
    get_highest_grade,
    get_lowest_grade,
    is_passed,
    display_report,
)

students = {"Yash": 90, "Rohit": 80, "Amit": 50}

if __name__ == "__main__":
    print("Initial Students and Grades:", students)
    add_student("Rahul", 85, students)
    print("Updated Students and Grades:", students)

    print("Average Grade: ", calculate_average(students))
    print("Highest Grade: ", get_highest_grade(students))
    print("Lowest Grade: ", get_lowest_grade(students))
    student_name = "Amit"
    if is_passed(student_name, students):
        print(f"{student_name} has passed.")
    else:
        print(f"{student_name} has failed.")

    print("\nStudent Report:")
    display_report(students)


