if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    # get the name of student from user
    query_name = input()
    # search name of student in dict and get the score
    marks = student_marks[query_name]
    # sum the marks
    sum_of_marks = sum(marks)
    # find the average
    avg = sum_of_marks/len(marks)
    # print the average
    print("{:.2f}".format(avg))
        
    