class Employee:

    company = "HCL"

    def __init__(self,id,name):
        self.id = id
        self.name = name

    def display(self):
        print(f"Id is : {self.id} \nName : {self.name}")
        print(f"Company:{Employee.company}")

emp1 = Employee(1,"Pushpa")
emp1.display()

emp2 = Employee(2,"Disha")
emp2.display()
    
        