def descending(people,scores):
    sorted_people = sorted(people, key=lambda person: scores[person[0]], reverse=True)
    return sorted_people
        
people = [('Alice', 30), ('Bob', 25), ('Charlie', 35)]
scores = {'Alice': 92, 'Bob': 88, 'Charlie': 95}

result = descending(people,scores)
print(result)



