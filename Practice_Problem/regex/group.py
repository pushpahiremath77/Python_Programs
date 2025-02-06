# import re
# s = "me tWelcome to GeeksForGeeks"
# res = re.findall(r"\D{2} t", s)

# print(res)
# print(res)

# string = "My name is disha"
# pattern = r'\disha'
# repl = 'pushpa'
# match = re.sub(pattern, repl, string)
# print(match)


# string = "123 "
# match = re.findall(r'\d\s',string)
# print(match)



# string = input("Enter")

# if re.match(r'^[A-Z][A-Za-z]+[@#%$^&*]\d+$', string):
#     print("Valid")
# else:
#     print("Invalid")


import re
text = "John (123-456-7890)"
match = re.search(r'(\w+) \((\d{3}-\d{3}-\d{4})\)', text)
if match:
    print(match.group())
    print(match.group(1))
    print(match.group(2))  
