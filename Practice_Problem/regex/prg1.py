import re

s = 'geeks.forgeeks'

# without using \
match = re.search(r'.', s)
print(match)

# using \
match = re.search(r'\.', s)
print(match)


s = 'for geeks.forgeeks portal and for the world'
# match = re.search(r'portal', s)
# print(match)
# print(match.start())
# print(match.end())
match = re.search(r'\Afor',s)
print(match)

print(match.re)
print(match.string)