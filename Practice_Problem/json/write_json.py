import json

data = {'name': 'Alice', 
        'age': 30, 
        'city': 'New York'
        }

with open('data.json','w') as file:
    json.dump(data,file,indent=4)


with open('data.json','r') as file:
    print(json.load(file))



import re

# Email string
email = "pushpahiremath72394@gmail.com"

# Regular expression to extract 'hiremath'
match = re.search(r'pushpa(.*?)\d+@', email)

# Check if there's a match and print the extracted part
if match:
    print(match.group(1))
else:
    print("No match found")



from collections import Counter

def most_frequent_char(s):
    frequency = Counter(s)
    return max(frequency, key=frequency.get)

# Example usage:
string = "banana"
print(most_frequent_char(string))





original = "hello world"
new = original.replace("world","python")
print(new)
print(original)










import re

def validate_email(email):
    pattern =r'^'