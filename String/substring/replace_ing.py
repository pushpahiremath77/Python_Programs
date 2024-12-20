def replace_ing(s):
    if len(s)<2:
        return s
    
    if s[-3:] == 'ing':
        s+='ly'
    else:
        s+='ing'

    return s

string = input("Enter a string:")
modified_string = replace_ing(string)
print(f"Replaced string is {modified_string}")