def find_sub_string(main_str,sub_str):
    return sub_str in main_str

main_str = input("Enter main string:")
sub_str = input("Enter substring:")

is_present = find_sub_string(main_str,sub_str)
print(is_present)
