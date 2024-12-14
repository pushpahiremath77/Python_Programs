def longer_words(list, n):
    result = []
    for word in list:
        if len(word) > n:
            result.append(word)
    return result

list = ['python', 'java', 'c', 'javascript', 'ruby', 'swift']
n = 5  

long_words = longer_words(list, n)
print(f"Words longer than {n} characters ---> ", long_words)
