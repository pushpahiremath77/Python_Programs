def remove_odd(s):
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:
            result = result + s[i]
    return result

string = input("Enter a string:")
removed = remove_odd(string)
print(f"After removed the char has odd index: {removed}")