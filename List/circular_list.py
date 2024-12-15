def circularly_identical(list1, list2):
  
    if len(list1) != len(list2):
        return False

    concatenated_list = list1 + list1
    
    if any(list2 == concatenated_list[i:i+len(list2)] for i in range(len(list1))):
        return True
    else:
        return False

list1 = [1, 2, 3, 4]
list2 = [3, 4, 1, 2]

result = circularly_identical(list1, list2)
print("Are the lists circularly identical?", result)
