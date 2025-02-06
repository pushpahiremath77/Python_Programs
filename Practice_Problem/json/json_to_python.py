import json

#json to python
json_data = '{"name": "Alice", "age": 30, "city": "New York"}'
print(type(json_data))
python_data = json.loads(json_data)
print(python_data)
print(type(python_data))


#python to json
data = json.dumps(python_data)
print(data)
print(type(data))

