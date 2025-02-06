def string_list(list1):
    new_list = []
    for item in list1:
        if len(item) > 5:
            new_list.append(item)
    return new_list

names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Bob", "Alice"]
new_list = string_list(names)
print(new_list)

