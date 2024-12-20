
def reverse_each_word(s):
    words = s.split()  
    reversed_words = [word[::-1] for word in words]  
    return ' '.join(reversed_words) 


string = input("Enter a string: ")


reversed_string = reverse_each_word(string)
print(f"Reversed words string: {reversed_string}")
