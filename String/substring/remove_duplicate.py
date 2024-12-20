def remove_duplicates(s):
    result = ""
    for char in s:
        if char not in result:
            result+=char
    return result

string1=input("Enter a string:")
result=remove_duplicates(string1)
print(f"Removed duplicate:{result}")
