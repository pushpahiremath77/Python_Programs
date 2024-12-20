def string_only_letter(s):
    return s.isalpha()

string1=input("Enter a string:")
is_letter = string_only_letter(string1)
print(is_letter)