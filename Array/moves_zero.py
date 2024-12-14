def move_zeroes(arr):
    count = 0 
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    
    while count < len(arr):
        arr[count] = 0
        count += 1
    return arr

arr = [0, 1, 9, 8, 0, 6, 0]
print(f"Array after moving zeroes: {move_zeroes(arr)}")
