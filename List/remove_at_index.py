def remove_elements(list):

    del list[5]  
    del list[4]  
    del list[0]  
    return list

list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

list = remove_elements(list)
print("List after removing elements --->", list)
