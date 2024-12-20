def extract_digit(s):
    digits = ""
    for char in s:
        if char.isdigit():
            digits += char
    return digits

string1=input("Enter a string:")
digits = extract_digit(string1)
print(f"Digits from string: {digits}")