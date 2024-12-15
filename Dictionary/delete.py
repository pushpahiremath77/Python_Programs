#using del statement
my_dict = {1: 10, 2: 20, 3: 30, 4: 40}
del my_dict[3]
print("After removing key 3:", my_dict)

#using pop()
removed_value = my_dict.pop(2, "Key not found")  
print("After removing key 2:", my_dict)
print("Removed value:", removed_value)