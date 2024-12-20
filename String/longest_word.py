def longest_word(s):
    words = s.split()
    long_word = max(words,key=len)
    length = len(long_word)
    return long_word,length

string1 = input("Enter a string: ")
longest_word, length_of_word = longest_word(string1)
print(f"Longest word in a string: {longest_word} with length {length_of_word}")