def gradingStudents(grades):
    for grade in grades:
        grade = int(grade)
        nearest_multiple = 5*round(grade/5)
        if nearest_multiple<grade:
            nearest_multiple=grade
        elif grade<38:
            nearest_multiple=grade
        print(nearest_multiple)

n= int(input("no of students: "))
grades = []
for i in range(n):
    grades.append(input("enter grade of student: "))
    
result = gradingStudents(grades)

