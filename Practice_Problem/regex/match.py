import re
pattern = r'a.b'
string = "abb axb xyx acb"
match = re.match(pattern,string)
print(match.group())



import re

text = "Contact me at john.doe@example.com."
match = re.search(r'\b[\w.-]+@[\w.-]+\.\w{2,4}\b', text)
if match:
    print(match.group())
else:
    print("No match")




import re
text = "Contact me at john.doe@example.com."
replace = "Bridgelabz"
match = re.sub(r'\b[\w.-]+@[\w.-]+\.\w{2,4}\b', replace , text)
print(match)


