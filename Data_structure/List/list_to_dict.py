#1
list1 = ['red', 'green', 'blue']
list2 = ['#FF0000', '#008000', '#0000FF']
dict1 = dict(zip(list1,list2))
print(dict1)
key_max = max(dict1.keys(), key=(lambda k: dict1[k]))
print(key_max)

key_min = min(dict1.keys(), key=(lambda k: dict1[k]))
print(key_min)


#2
dict1 = {}
if not bool(dict1):
    print("Dictionary is empty")


#3
def tuple_dict(data):
    result = []
    for tuple in data:
        for i in range(0,len(tuple),2):
            result.append({tuple[i]:tuple[i+1]})
    return result

data = [("id", 1, "name", "Alice"), ("id", 2, "name", "Bob")]
result = tuple_dict(data)
print(result)


#4
data = [("id", 1, "name", "Alice"), ("id", 2, "name", "Bob")]
result = []
for item in data:
    result.append({item[i]: item[i + 1] for i in range(0, len(item), 2)})
print(result)



#4
data = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}, {"id": 1, "name": "Alice"}]
new = set()
for dict1 in data:
    if dict1["id"] not in new:
        new.add(dict1["id"])
print(new)



#5
#{'Alice': 88.5, 'Bob': 83.0, 'Charlie': 97.5}
def average_score(data):
    dict1 = {}
    for name,marks in data['students']:
        average = sum(marks)/len(marks)
        dict1[name] = average
    return dict1

data = {'students': [('Alice', [85, 92]), ('Bob', [78, 88]), ('Charlie', [95, 100])]}
result = average_score(data)
print(result)
