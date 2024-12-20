
def count_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

string = input("Enter a string: ")
char_count = count_characters(string)
print("Character occurrences:")
for char, count in char_count.items():
    print(f"{char}: {count}")
