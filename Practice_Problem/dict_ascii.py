def to_dict(list1):
    new_dict = {}
    for item in list1:
        new_dict[item]=ord(item)
    return new_dict

list1 = ["A", "B", "C","^"]
result = to_dict(list1)
print(result)