def reverse_string(s):
    reversed = ""
    for char in s:
        reversed = char + reversed
    print(f"Reversed string: {reversed}")

string1 = input("Enter a string:")
reverse_string(string1)