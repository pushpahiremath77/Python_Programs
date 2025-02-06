my_set = {1, 2, 3, 4, 5}
item = 3
if item in my_set:
    my_set.remove(item)
    print(f"Removed {item}: ", my_set)
else:
    print(f"{item} not present in set.")

print("****************")
# set1 = {1,2,3,4,5,6}
# set2 = {6,7,3,9,10}
# print(f"Set1: {set1}")
# print(f"Set2: {set2}")
# for item in set1:
#     if item in set2:
#         print(f"Intersection of sets: {item}")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection = set1.intersection(set2)
print("Intersection:", intersection)

print("*******************")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union = set1.union(set2)
print("Union:",union)

print("*******************")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
difference = set1.difference(set2)
print("Difference:",difference)

print("*******************")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
symmetric_difference = set1.symmetric_difference(set2)
print("Symmetric difference:",symmetric_difference)

print("*******************")
set1 = {1,2,3,4,5}
set1.clear()
print(f"Cleared set: {set1}")

print("*******************")
my_frozenset = frozenset([1, 2, 3, 4, 5])
print("Frozenset:", my_frozenset)

print(type(my_frozenset))

minimum = min(my_frozenset)
print(f"Minimum:{minimum}")

maximum = max(my_frozenset)
print(f"Maximum:{maximum}")