def find_max(list):
    max_value = list[0]
    for num in list:
        if num > max_value:
            max_value = num
    return max_value

list = [2, 8, 1, 6, 4]
print("Maximum value:", find_max(list)) 
