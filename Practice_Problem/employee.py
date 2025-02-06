import random

class Company:
    def __init__(self, name):
        self.name = name
        self.employees = [] 
        self.employee_ids = set() 

    def generate_empid(self):
        while True:
            emp_id = random.randint(1, 3)  
            if emp_id not in self.employee_ids:  
                self.employee_ids.add(emp_id)  
                return emp_id

    def add_employee(self, name, department):
        emp_id = self.generate_empid()
        new_employee = Employee(emp_id, name, department)
        self.employees.append(new_employee)
        return new_employee

    def list_employees(self):
        return [str(emp) for emp in self.employees]

class Employee:
    def __init__(self, emp_id, name, department):
        self.emp_id = emp_id
        self.name = name
        self.department = department

    def __str__(self):
        return f"Employee[ID={self.emp_id}, Name={self.name}, Department={self.department}]"

if __name__ == "__main__":
    my_company = Company("TechCorp")

    emp1 = my_company.add_employee("Alice", "Engineering")
    emp2 = my_company.add_employee("Bob", "HR")
    emp3 = my_company.add_employee("Charlie", "Marketing")

    print("Employees in the company:")
    for emp in my_company.list_employees():
        print(emp)
