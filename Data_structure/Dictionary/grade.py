def create_nested():
    student = {}
    n = int(input("Enter number of students:"))
    for i in range(1,n+1):
        s_name = input(f"Enter name of student {i}:")
        maths = int(input("Enter maths marks:"))
        science = int(input("Enter science marks:"))
        english = int(input("Enter english marks:"))

        student[s_name] = {'Maths':maths,'Science':science,'English':english} 
    return student


def average_grade(student):
    for name,marks in student.items():
        average_marks = (marks['Maths']+marks['Science']+marks['English'])/3
        if average_marks >= 90:
            student[name]['Grade']='A'
        elif average_marks>=75 and average_marks<90:
            student[name]['Grade']='B'
        elif average_marks>=50 and average_marks<75:
            student[name]['Grade']='C'
        else:
            student[name]['Grade']='Fail'
    return student


student_data = create_nested()
grade = average_grade(student_data)
print(grade)