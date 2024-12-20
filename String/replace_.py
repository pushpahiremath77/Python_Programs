def replace_underscore(s):
    return s.replace(' ','_')

string1 = input("Enter a string: ")
replaced = replace_underscore(string1)
print(f"Replace space with _ : {replaced}")
