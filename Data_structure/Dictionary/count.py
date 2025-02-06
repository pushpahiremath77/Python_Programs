def count_dict(dict_list):
    count = 0
    for dict in dict_list:
        if 'success' in dict and dict['success'] == True:
            count+=1
    return count

data = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}] 
result = count_dict(data)
print(result)