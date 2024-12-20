def anagram(s1,s2):
    return sorted(s1) == sorted(s2)

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if anagram(s1,s2):
    print(f"{s1} & {s2} are Anagram")
else:
    print(f"{s1} & {s2} are not Anagram")