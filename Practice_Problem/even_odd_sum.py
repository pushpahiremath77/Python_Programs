list1 = [-1, -2, -3, -4, -5, -6]
even_sum = 0
odd_sum = 0
new = []
for item in list1:
    if item%2==0:
        even_sum+=item
    else:
        odd_sum+=item
new.append(even_sum)
new.append(odd_sum)
print(new)