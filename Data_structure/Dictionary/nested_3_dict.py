def create_nested():
    student = {}
    n = int(input("Enter number of students:"))
    for i in range(1,n+1):
        s_name = input(f"Enter name of student {i}:")
        dept = input(f"Enter department of {s_name}:")
        maths = int(input("Enter maths marks:"))
        science = int(input("Enter science marks:"))
        english = int(input("Enter english marks:"))

        student[s_name] ={
                            'Department':dept,
                            'Marks':{
                                    'Maths':maths,
                                    'Science':science,
                                    'English':english
                                    } 
                            }
    return student

students = create_nested()
print(students)