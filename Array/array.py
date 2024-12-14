
import array

arr = array.array('i', [1, 2, 3])
print("Original Array:", arr)

arr.append(4)
print("Array after appending:", arr)

#Removes element 2
arr.remove(2)
print("Array after removing:", arr)

#insert element 5 at position 1
arr.insert(1, 5)
print("Array after inserting 5 at position 1:", arr)

#Removes the last element
popped_element = arr.pop()
print("Popped Element:", popped_element)
print("Array after popping:", arr)

#Reverse the array
arr.reverse()
print("Reversed Array:", arr)

buffer_info = arr.buffer_info()
print("Memory Info:", buffer_info)


#sorting
arr = sorted(arr)
print("Array after sorting:", arr)
