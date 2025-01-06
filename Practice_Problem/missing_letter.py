def get_missing_letter(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    missing_letters = [letter for letter in alphabet if letter not in string]
    return "".join(missing_letters)

print(get_missing_letter("abcdefgpqrstuvwxyz"))