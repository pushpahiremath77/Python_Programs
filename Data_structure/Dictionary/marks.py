def create_dict(data):
    result = {}
    for (sub,name),marks in data.items():
        if name not in result:
            result[name] ={}     
        result[name][sub] = marks
    return result

data = {('Math', 'Alice'): 85, ('Science', 'Bob'): 78, ('Math', 'Charlie'): 95, ('Science', 'Alice'): 92}
result = create_dict(data)
print(result)