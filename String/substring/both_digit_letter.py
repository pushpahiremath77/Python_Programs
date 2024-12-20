def both_letter_digit(s):
    return any(char.isalpha() for char in s) and any(char.isdigit() for char in s)


string1=input("Enter a string:")
is_both = both_letter_digit(string1)
print(is_both)