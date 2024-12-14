import array

arr = array.array('i', [10, 20, 30, 40, 50])

sliced_arr = arr[:5]

print("Sliced Array:")
for item in sliced_arr:
    print(item)
