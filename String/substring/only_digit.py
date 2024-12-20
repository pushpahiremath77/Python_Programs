def string_only_digit(s):
    return s.isdigit()

string1=input("Enter a string:")
is_digit = string_only_digit(string1)
print(is_digit)