# Program to swap two tuples
tuple1 = (1, 2)
tuple2 = (3, 4)

# Swapping using tuple unpacking
tuple1, tuple2 = tuple2, tuple1
print("Tuple1:", tuple1)
print("Tuple2:", tuple2)

# Program to convert a tuple of tuples to a dictionary
tuple_of_tuples = (('key1', 'value1'), ('key2', 'value2'))
my_dict = dict(tuple_of_tuples)
print("Dictionary:", my_dict)

# Program to zip two lists into a tuple
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped_tuple = tuple(zip(list1, list2))
print("Zipped tuple:", zipped_tuple)

print("********************")

tuplex = (4, 6, 2, 8, 3, 1)
print(tuplex)

tuplex = tuplex + (9,)
print(tuplex)

tuplex = tuplex[:5] + (15, 20, 25) + tuplex[:5]
print(tuplex)

listx = list(tuplex)
listx.append(30)
tuplex = tuple(listx)
print(tuplex) 
