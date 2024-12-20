def extract_letter(s):
    letters = ""
    for char in s:
        if char.isalpha():
            letters += char
    return letters

string1=input("Enter a string:")
letters = extract_letter(string1)
print(f"Letters from string: {letters}")