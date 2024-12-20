def replace_sapce(s):
    return s.replace(" ","")

string1 = input("Enter a string:")
space = replace_sapce(string1)
print(f"After removed space: {space}")