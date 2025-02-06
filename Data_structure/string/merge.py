def merge_words(word1,word2):
    i, j = 0, 0
    result = []
    while i<len(word1) and j<len(word2):
        result.append(word1[i])
        result.append(word2[j])
        i+=1
        j+=1  
    result.extend(word1[i:])
    result.extend(word2[j:])
    
    return ''.join(result)

word1 = "abc"
word2 = "pqr"
result = merge_words(word1,word2)
print(result)