def replace_vowels(s):
    vowels = 'aeiouAEIOU'
    replaced = ""
    for char in s:
        if char in vowels:
            replaced+='*'
        else:
            replaced+=char
    return replaced

string1 = input("Enter a string: ")
replaced = replace_vowels(string1)
print(f"Replaced vowel with '*' : {replaced}")
    
    