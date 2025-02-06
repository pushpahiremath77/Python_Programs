set1 = {10,20,30,40}
print(f"Set: {set1}")

my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)

set2 = {1, 2, 3, 4, 5}
set2.add(6)
print(set2)

set2.update([7,8,9])
print("After adding multiple members:", set2)

set2.remove(6)
print(set2)

set2.discard(9)
print(set2)
