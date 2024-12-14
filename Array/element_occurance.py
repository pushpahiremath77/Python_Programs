import array
arr = array.array('i', [10, 20, 30, 40, 20, 50, 30, 60,20])
element = 20
count = arr.count(element)
print(f"The number of occurrences of {element} in the array is: {count}")