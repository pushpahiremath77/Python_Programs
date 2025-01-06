def pluralize_words(list1):
    result = set()
    new_dict = {}
    for item in list1:
        if item not in new_dict:
            new_dict[item]=1
        else:
            new_dict[item]+=1
    
    for key,value in new_dict.items():
        if value>1:
            result.add(key+"s")
    return result

list1 = ["cow", "pig", "cow", "cow","pig"]
result = pluralize_words(list1)
print(result)