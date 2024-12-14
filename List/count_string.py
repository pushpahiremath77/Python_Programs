def count_string(list):
    count=0
    for str in list:
        if len(list)>=2 and str[0]==str[-1]:
            count+=1
    return count

list = ['abc', 'xyz', 'aba', '1221']
result = count_string(list)
print("Number of strings first and last character are same:", result)











# def count_matching_strings(string_list):
#     count = 0
#     for s in string_list:
#         if len(s) >= 2 and s[0] == s[-1]:
#             count += 1
#     return count

# sample_list = ['abc', 'xyz', 'aba', '1221']
# result = count_matching_strings(sample_list)
# print("Expected Result:", result)
