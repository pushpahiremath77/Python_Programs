import array

arr = array.array('i', [25, 11, 79, 75, 56])

largest_element = arr[0]

for num in arr:
    if num > largest_element:
        largest_element = num

print("Array:", arr)
print("Largest element in the array:", largest_element)
