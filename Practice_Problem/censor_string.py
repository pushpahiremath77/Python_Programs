def uncensor(string,vowel):
    result = []
    vowel_index = 0
    for char in string:
        if char=="*":
            result.append(vowel[vowel_index])
            vowel_index+=1
        else:
            result.append(char)
    return "".join(result)

string = "Wh*r* d*d my v*w*ls g*?"
vowel = "eeioeo"
result = uncensor(string,vowel)
print(result)