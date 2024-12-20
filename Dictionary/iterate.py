my_dict = {'a': 1, 'b': 2, 'c': 3}

#Key
for key in my_dict:
    print(f"Key: {key}")
print()

#Value
for value in my_dict.values():
    print(f"Value: {value}")
print()

#Key-value pairs
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")
print()

#Access values using key
for key in my_dict:
    print(f"Key: {key}, Value: {my_dict[key]}")

for key,value in my_dict.items():
    print(f"{key}-->{value}")