def vowel_links(txt):
    vowels = "aeiou"
    words = txt.split()
    for i in range(len(words)-1):
        if words[i][-1] in vowels and words[i+1][0] in vowels:
            return True
    return False

string = "a very large appliance"   
result = vowel_links(string)
print(result)