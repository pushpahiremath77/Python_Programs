s1 = "Pushpaabc"
s1 = set(s1)
print(s1)
s2 = "Pushpash"
s2 = set(s2)
print(s2)
difference = s1.difference(s2)
#difference = s1 & s2
union = s1.union(s2)
#union = s1 | s2
print(union)
print(difference)