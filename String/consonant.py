def count_consonant(s):
    vowels = 'aeiouAEIOU'
    count=0
    for char in s:
        if char not in vowels:
            count+=1
    return count

string1 = input("Enter a string: ")
cons_count = count_consonant(string1)
print(f"Count of consonants in string: {cons_count}")