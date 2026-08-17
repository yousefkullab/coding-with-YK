
def add_student(name, grade, students):
    students[name] = grade

def calculate_average(students):
    if not students:
        return 0
    total = sum(students.values())
    return total / len(students)

def get_highest_grade(students):
    if not students:
        return None, 0
    highest_grade = max(students.values())
    for name, grade in students.items():
        if grade == highest_grade:
            return name, grade

def get_lowest_grade(students):
    if not students:
        return None, 0
    min_grade = min(students.values())
    for name, grade in students.items():
        if grade == min_grade:
            return name, grade

def is_passed(name, students):
    if name in students:
        return students[name] >= 60


def display_report(students):
    for name, grade in students.items():
        status = "Passed" if grade >= 60 else "Failed"
        print(f"Student: {name},\tGrade: {grade},\tStatus: {status}")



