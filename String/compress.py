def compress_string(s):
    if not s:
        return ""
    
    compressed = []
    count = 1
  
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
    compressed.append(s[-1] + str(count))
    compressed_string = ''.join(compressed)
    return compressed_string if len(compressed_string) < len(s) else s

print(compress_string("aaabbcc"))   
print(compress_string("abcd"))      
print(compress_string("aabcccccaaa")) 
print(compress_string(""))           









# Function to create a nested dictionary for n students
def create_student_data(n):
    student_data = {}

    # Iterate for n students
    for i in range(1, n + 1):
        student_name = f"s_name{i}"  # Name format: s_name1, s_name2, etc.
        python_score = int(input(f"Enter Python score for {student_name}: "))
        java_score = int(input(f"Enter Java score for {student_name}: "))
        
        # Add the student's data to the dictionary
        student_data[student_name] = {"python": python_score, "java": java_score}

    return student_data

# Example usage
n = int(input("Enter the number of students: "))
students = create_student_data(n)

# Print the result
print("\nStudent Data:", students)
