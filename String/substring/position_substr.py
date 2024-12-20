def position_substring(main_str, sub_str):
    return main_str.find(sub_str)

main_str = input("Enter the main string: ")
sub_str = input("Enter the substring: ")

position = position_substring(main_str, sub_str)
print(f"The substring {sub_str} occurs at position {position} .")
