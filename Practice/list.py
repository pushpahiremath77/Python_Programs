list1 = [1,2,3,4,2,6,5]

largest = max(list1)
print(largest)

smallest=min(list1)
print(smallest)

max = list1[0]
for item in list1:
    if item > max:
        max = item
print(f"Max:{max}")

min = list1[0]
for item in list1:
    if item < min:
        min = item
print(f"Min:{min}")



large = float('-inf')
s_large = float('-inf')
for ietm in list1:
    if item>large:
        large = item
        s_large=large
print(f"Second largest: {s_large}")


print(list1.index(5))

item = 7
if item in list1:
    print("present")
else:
    print("not present")
        
        