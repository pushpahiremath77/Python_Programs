# def create_histogram(int_list):
#     for num in int_list:
#         print('*' * num)
# int_list = [3, 5, 7, 2, 1]
# create_histogram(int_list)

# print("*********************************")
# def concatenate_list_elements(input_list):
    
#     return ''.join(map(str, input_list))

# input_list = [1, 'apple', 3, 'banana', 5]

# result = concatenate_list_elements(input_list)
# print("Concatenated string:", result)

# my_dict = {2: 10, 1: 20, 5: 30, 3: 40, 4: 50}
# asc_dict = dict(sorted(my_dict.items()))
# print("Ascending order:", asc_dict)

# desc_dict = dict(sorted(my_dict.items(), reverse=True))
# print("Descending order:", desc_dict)


# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}

# my_dict = {**dic1, **dic2, **dic3}
# print(f"concatenated dictionary: {my_dict}")

# for key in my_dict:
#     print(key, end=" ")
   
# for value in my_dict.values():
#     print(value,end=" ")

# for key,value in my_dict.items():
#     print(f"{key}:{value}")


#Nested dictionary
list = [1,2,3,4,5]
nested_dict = current = {}
for item in list:
    current[item]={}
    current = current[item]
print("Nested dictionary:", nested_dict)











