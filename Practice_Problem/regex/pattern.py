import re
text = '''John Doe mentioned that the key stakeholder, Alice Williams (alice.williams@businesscorp.com), will be 
unavailable from April 5, 2025, to April 15, 2025, due to personal commitments. We need to ensure that the initial 
review is completed before her absence.David shared some concerns about server infrastructure, which need to be 
addressed before the testing phase. He recommended that we contact the support team (support@hostingprovider.com) to 
resolve these issues by April 20, 2025.Additionally, Sarah pointed out that a client demo has been scheduled for 
May 1, 2025, with potential investors. It's critical to finalize the prototype by April 28, 2025. For any follow-up 
queries, please reach out to her at sarah.connor@company.org.'''


pattern = re.compile(r'[a-z]+\.[a-z]+@[a-z]+\.[a-z]{3}')
matches = pattern.finditer(text)
for match in matches:
    print(match.group())


text = "Hello, World Hello!"
pattern = r"Hello"
match = re.search(pattern, text)
print(match.group())



text = "Email: user@example.com"
pattern = r"\w+@\w+\.\w+"
match = re.search(pattern, text)
print(match.group())



text = "Python is fun and powerful."
pattern = r"\b\w+\b"
words = re.findall(pattern,text)
print(words)




text = "I like cats. Cats are great!"
pattern = r'cats'
replacement = "dogs"
new_text = re.sub(pattern,replacement,text,flags=re.IGNORECASE)
print(new_text)



import re

text = "Contact me at john.doe@example.com or at admin@my-site.org for more information."
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
emails = re.findall(pattern, text)
print(emails)
