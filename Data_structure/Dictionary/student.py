def create_student_data():
    student_data = {}
    num_students = int(input("Enter the number of students: "))

    for _ in range(num_students):
        student_name = input("Enter the student's name: ")
        python_marks = int(input(f"Enter {student_name}'s Python marks: "))
        java_marks = int(input(f"Enter {student_name}'s Java marks: "))
        devops_marks = int(input(f"Enter {student_name}'s DevOps marks: "))

        student_data[student_name] = {
            'Python': python_marks,
            'Java': java_marks,
            'DevOps': devops_marks
        }
    return student_data

def calculate_average(student_data):
    for student, marks in student_data.items():
        avg_marks = (marks['Python'] + marks['Java'] + marks['DevOps']) / 3
        student_data[student]['Average'] = avg_marks
    return student_data

student_data = create_student_data()
student_data_with_avg = calculate_average(student_data)

print("\nStudent Data with Averages:")
for student, details in student_data_with_avg.items():
    print(f"{student}: {details}")
