def convert_string(str1):
    dict1 = {}
    for item in str1:
        if item in dict1:
            dict1[item]+=1
        else:
            dict1[item] = 1
    return dict1 

str1 = 'w3resource' 
converted = convert_string(str1)
print(converted)