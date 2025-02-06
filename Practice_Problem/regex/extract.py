import re
text = "Event on 2024-12-31, another on 2023-07-25."
pattern = r'\d{4}-\d{2}-\d{2}'
match = re.findall(pattern,text)
print(match)


text = "Happy sheep swimming"
matches = re.findall(r'\b\w*(\w)\1\w*\b', text)
print(matches)



text = "My phone 143-456-7890 number is 123-456-7890"
pattern = r'(\d{3})-(\d{3})-(\d{4})'

match = re.findall(pattern, text)
print(match[0])







import re

def before_and_after_pattern(text, pattern):
    match = re.search(pattern, text)
    
    if match:
        before = text[:match.start()]  
        after = text[match.end():]    
        return before, after
    else:
        return "Pattern not found", "Pattern not found"


text = "The quick brown fox jumps over the lazy dog."
pattern = r'fox'  
before, after = before_and_after_pattern(text, pattern)
print("Before:", before)  
print("After:", after)    







import re

def find_all_matches(text, pattern):
    return re.findall(pattern, text)

# Example usage
text = "The quick brown fox jumped over the lazy fox."
pattern = r'\b\w{3}\b'  # Pattern to match the word 'fox'
matches = find_all_matches(text, pattern)
print(matches)  # Output: ['fox', 'fox']
