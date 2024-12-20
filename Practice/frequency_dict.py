string = "Programming"
dict1 = {}
for char in string:
    if char in dict1:
        dict1[char]+=1
    else:
        dict1[char]=1
print(dict1)