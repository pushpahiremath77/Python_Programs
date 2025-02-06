def create_dict(keys, values):
    return dict(zip(keys, values))

keys = ['name', 'age']
values = ['Alice', 25]
result = create_dict(keys, values)
print(result)
