def avg(values):
    return sum(values) / len(values)


number_students = int(input())
students_strings = [input() for _ in range(number_students)]

students_grades = {}

for student_str in students_strings:
    student, grade_str = student_str.split()
    grade = float(grade_str)
    if student not in students_grades:
        students_grades[student] = []

    students_grades[student].append(grade)

for student, grades in students_grades.items():
    grades_formatted = " ".join(f"{grade:.2f}" for grade in grades)
    avg_grade = f"{avg(grades):.2f}"  # <-- WHY HERE the return type is STRING ??? Because we use f-string interpolation
    print(f"{student} -> {grades_formatted} (avg: {avg_grade})")