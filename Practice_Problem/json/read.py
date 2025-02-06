with open('example.txt', 'w') as file:
    file.write("Pramod , Pushpa")  
    
# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)

with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip()) 

#     line = file.readline()
#     print(line)

# with open('example.txt', 'a') as file:
#     file.write(" How are you")  



# with open('example.txt', 'w') as file:
#     file.write("Hello, World!")


# data = {'name': 'John', 'age': 30}


# import json

# with open('data.json', 'r') as file:
#     data = json.load(file)
#     print(data)
#     print(data['name'])

# with open('data.json', 'w') as file:
#     json.dump(data, file)
