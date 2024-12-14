def common_element(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 3, 9, 10]

result = common_element(list1, list2)

print("Lists have a common element? --->", result)
