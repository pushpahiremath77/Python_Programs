def list_to_nested_dict(input_list):
    nested_dict = {}
    current_dict = nested_dict
    for item in input_list:
        current_dict[item] = {}
        current_dict = current_dict[item]  
    
    return nested_dict

input_list = ['a', 'b', 'c', 'd']
result = list_to_nested_dict(input_list)

print("Nested dictionary:", result)
