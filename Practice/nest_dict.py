nested_dict = {
    "employee1": {"name": "John", "age": 30, "department": "HR"},
    "employee2": {"name": "Alice", "age": 25, "department": "Finance"},
    "employee3": {"name": "Bob", "age": 35, "department": "IT"}
}


print("Employee 1 Name:", nested_dict["employee1"]["name"])  

print("Iterating over the nested dictionary:")
for employee, details in nested_dict.items():
    print(f"Details of {employee}:")
    for key, value in details.items():
        print(f"  {key}: {value}")
    print()


nested_dict["employee1"]["age"] = 31
print("Updated Nested Dictionary:", nested_dict)


nested_dict["employee4"] = {"name": "Charlie", "age": 28, "department": "Marketing"}
print("Nested Dictionary after adding a new employee:", nested_dict)


del nested_dict["employee2"]["age"]
print("Nested Dictionary after deletion:", nested_dict)
