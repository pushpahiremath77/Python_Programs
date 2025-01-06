title = "ZY"
result = 0
for char in title:
    value = ord(char) - ord('A') + 1
    result = result*26+value
print(result)