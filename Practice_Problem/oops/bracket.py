def validate_brackets(string):
    stack = []
    brackets = {'(':')','{':'}','[':']'}
    for char in string:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
    return len(stack) == 0
string = input("Enter string:")
result = validate_brackets(string)
print(result)
























