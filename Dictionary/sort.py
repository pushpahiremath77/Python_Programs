my_dict = {3: 'apple', 1: 'banana', 2: 'cherry'}

ascending_dict = dict(sorted(my_dict.items()))

descending_dict = dict(sorted(my_dict.items(), reverse=True))

print("Original Dictionary:", my_dict)
print("Dictionary sorted in ascending order by key:", ascending_dict)
print("Dictionary sorted in descending order by key:", descending_dict)
