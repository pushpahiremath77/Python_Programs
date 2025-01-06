def get_highest(alphabet,name):
    highest_index = -1
    highest_letter = ""
    for char in name:
        if char in alphabet:
            index = alphabet.index(char) + 1
            if index>highest_index:
                highest_index = index
                highest_letter = char
    return f"{highest_index}{highest_letter}"

alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", 
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
name = "pushpa"
result = get_highest(alphabet,name)
print(result)