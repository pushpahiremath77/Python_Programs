def fist_last_char(string1):
    count = 0
    for word in string1:
        if len(word)>=2 and word[0]==word[-1]:
            count+=1
    return count
        

string1 = ['abc','1221','psh','aba']
repeated = fist_last_char(string1)
print(repeated)