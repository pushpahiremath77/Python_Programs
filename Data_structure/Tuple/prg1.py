tuple1 = (1,2,3,4,5,2,3,2,2)
print(tuple1)
element = 6
if element in tuple1:
    print(f"{element} is present in tuple")
else:
    print(f"{element} is not present in tuple")

print(tuple1.count(5))
print(tuple1.index(5))

def repeated_items(tuple1):
    count_dict = {}
    for item in tuple1:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    repeated = [count for item,count in count_dict.items() if count>1]
    return repeated

tup1 = (1,2,3,4,5,2,3,2,4,2,3)
repeated = repeated_items(tup1)
tuple2 = tuple(repeated)
print(tuple2)