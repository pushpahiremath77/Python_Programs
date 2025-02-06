# def convert_to_dict(list1):
#     dict1 = {}
#     for list_item in list1:
#         for i in range(len(list_item)):
#             dict1[list_item[i]] = list_item[i+1]
#     return dict1

# list1 = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
# dictionary = convert_to_dict(list1)
# print(dictionary)



def convert_to_dict(list1):
    dict1 = {}
    for key, value in list1:
        dict1[key] = value
    return dict1

list1 = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
dictionary = convert_to_dict(list1)
print(dictionary)
