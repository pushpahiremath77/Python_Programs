import array

arr1 = array.array('i', [40, 50, 60])
arr2 = array.array('i', [27, 98])

arr1.extend(arr2)

print("Extended Array:")
for item in arr1:
    print(item)
