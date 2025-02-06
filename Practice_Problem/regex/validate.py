import re
string = "pushpa@gmail.com is my email id"
pattern = r'[\w\.-]+@[\w\.-]+\.\w{2,4}'
match = re.search(pattern,string)
print(match)


import re
string = input("Enter email:")
pattern = r'[\w\.-]+@[\w\.-]+\.\w{2,4}'
if re.search(pattern,string):
    print("Valid email")
else:
    print("Invalid email")