grades = [85, 72, 90, 55, 68, 40, 95]

def calculate_avg(grades):
    sum = 0
    for grade in grades:
        sum += grade
    avg = sum/len(grades)
    return avg

def find_max(grades):
    max = grades[0]
    for grade in range(len(grades)):
        if grades[grade] > max:
            max = grades[grade]
    return max


def count_passed(grades):
    count = 0
    for grade in grades:
        if grade >= 60:
            count += 1
    return count

def get_grade_status(grades):
    status = []
    for grade in grades:
        if grade >= 90:
            status.append("Excellent")
        elif grade >=80:
            status.append("Very Good")
        elif grade >=70:
            status.append("Good")
        elif grade >=60:
            status.append("Pass")
        else:
            status.append("Fail")
    return status

print(f"Avarage: {calculate_avg(grades)}")
print(f"Highest: {find_max(grades)}")
print(f"Passed Students: {count_passed(grades)}")

status = get_grade_status(grades)
print("Grade Report: ")
for grade, status in zip(grades, status):
     print(f"{grade} → {status}")


