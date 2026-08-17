
def get_second_grade(students):
    grade = lambda grades: grades[1]
    students.sort(key=grade)
    grades_set = set()
    for i in students:
        grades_set.add(i[1])
    grades_list = list(grades_set)
    grades_list.sort()
    if len(grades_list) >= 2:
        return grades_list[1]
    else:
        return grades_list[0]


if __name__ == '__main__':
    students = []
    for _ in range(int(input("N: "))):
        name = input("name: ")
        score = float(input("score: "))
        students.append([name, score])
    second_grade = get_second_grade(students)
    result = []
    for s in students:
        if s[1] == second_grade:
            result.append(s)    
    result.sort()
    for i in result:
        print(i[0])

# Software Engineer Joseph
