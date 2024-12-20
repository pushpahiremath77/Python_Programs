def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count+=1
    return count

string1=input("Enter a string:")
vowel_count = count_vowels(string1)
print(f"{vowel_count}")