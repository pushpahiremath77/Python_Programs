def count_substring(main_str, sub_str):
    return main_str.count(sub_str)

main_str = input("Enter the main string: ")
sub_str = input("Enter the substring: ")

count = count_substring(main_str, sub_str)
print(f"The substring occurs {count} times.")
