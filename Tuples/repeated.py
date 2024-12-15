# my_tuple = (1, 2, 3, 1, 4, 2, 5, 6, 2)
# repeated_items = [item for item in set(my_tuple) if my_tuple.count(item) > 1]
# print("Repeated items:", repeated_items)


tuple = (1, 2, 3, 1, 4, 2, 5, 6, 2)
repeated_items = []
for item in tuple:
    if tuple.count(item) > 1 and item not in repeated_items:
        repeated_items.append(item)
print("Repeated items:", repeated_items)
