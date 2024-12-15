tuple = (1, 2, 3, 4, 5)
print(tuple)

#Different data types
mixed_tuple = (1, "Hello", 3.14, True)
print(mixed_tuple)

#unpack
a,b,c,d = mixed_tuple
print(f"a:{a}, b:{b}, c:{c}, d:{d}")


#Slicing
my_tuple = (1, 2, 3, 4, 5, 6)
slice_tuple = my_tuple[2:5]  
print(slice_tuple)
