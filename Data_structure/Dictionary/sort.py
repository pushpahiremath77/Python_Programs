my_dict = {3: 'apple', 1: 'banana', 2: 'cherry'}
ascending = dict(sorted(my_dict.items()))
descending = dict(sorted(my_dict.items(), reverse=True))
print(ascending)
print(descending)