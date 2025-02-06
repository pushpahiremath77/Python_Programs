#[(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
data = {'a': [(1, 2), (3, 4)], 'b': [(5, 6)], 'c': [(7, 8), (9, 10)]}
list1 = []
for key in data:
    list1.extend(data[key])
print(list1)