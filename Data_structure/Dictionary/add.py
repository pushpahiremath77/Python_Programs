dict1 = {0: 10, 1: 20} 
dict1[2] = 30
dict1[3] = 40
print(dict1)

dic1={1:10, 2:20}  
dic2={3:30, 4:40}  
dic3={5:50,6:60} 
result = {**dic1, **dic2, **dic3}
print(result)


new_dict = {x:x*x for x in range(1,6)}
#new_dict = {x:x**2 for x in range(1,6)}
print(new_dict)
new_dict.pop(4)
print(new_dict)
new_dict.popitem()
print(new_dict)

def unique_values(data):
    unique = set() 
    for dict in data:
        for value in dict.values():
            unique.add(value)
    return unique

data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}] 
unique = unique_values(data)
print(unique)
    





dictionary = {'a':10,'b':20,'c':30,'d':40}
# sum = sum(dictionary.values())
# print(sum)

sum = 0
for value in dictionary.values():
    sum+=value
print(sum)

product = 1
for value in dictionary.values():
    product*=value
print(product)

dictionary.pop('c')
print(dictionary)