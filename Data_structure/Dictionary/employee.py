def create_nested():
    employee = {}
    n = int(input("Enter number of employees:"))
    for i in range(1, n + 1):
        emp_name = input(f"Enter name of Employee {i}:")
        base_salary = float(input("Enter base salary:")) 
        bonus = float(input("Enter bonus:"))
        tax = float(input("Enter tax:"))
        employee[emp_name] = {'Base_salary': base_salary,
                              'Bonus': bonus,
                              'Tax': tax}
    return employee

def cal_net_salary(employee):
    for emp, sal in employee.items():
        net_salary = sal['Base_salary'] + sal['Bonus'] - sal['Tax']
        employee[emp]['Net_salary'] = net_salary
    return employee 

dict1 = create_nested()
dict2 = cal_net_salary(dict1)
print(dict2)
