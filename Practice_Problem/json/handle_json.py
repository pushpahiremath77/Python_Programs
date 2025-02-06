import json

try:
    with open('invalid.json', 'r') as file:
        data = json.load(file)
except json.JSONDecodeError:
    print("Error parsing JSON!")
