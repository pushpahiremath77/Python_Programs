import array

arr = array.array('i', [10, 20, 30, 40, 50])

popped_element = arr.pop(2)

print(f"Popped element: {popped_element}")
print("Array after pop:",arr)

