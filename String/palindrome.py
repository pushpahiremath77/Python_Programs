def check_palindrome(s):
    n = len(s)
    for i in range(n//2):
        if s[i] == s[n-i-1]:
            return True
    return False

string1 = input("Enter a string: ")
if check_palindrome(string1):
    print(f"{string1} is a Palindrome string")
else:
    print(f"{string1} is not a Palindrome string")