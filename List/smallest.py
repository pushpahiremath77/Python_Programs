def find_smallest(list):
    
    # smallest = min(list)
    # return smallest

    min_value = list[0]
    for num in list:
        if num < min_value:
            min_value = num
    return min_value

my_list = [3, 8, 1, 10, 15, 6]
smallest = find_smallest(my_list)
print(f"Smallest element --> {smallest}")