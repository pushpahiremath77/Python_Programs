import calendar
year = int(input("Enter year:"))
month = int(input("Enter month:"))
day = int(input("enter day:"))
print("\n", calendar.month(year, month,day))


# from datetime import date
# date1 = date(2014, 7, 2)
# date2 = date(2014, 7, 11)

# difference = date2 - date1

# print(f"{difference.days} days")

# print("***************")

# def is_value_in_group(value, group):
#     return value in group

# test_value1 = 3
# group = [1, 5, 8, 3]
# result1 = is_value_in_group(test_value1, group)
# print(f"{test_value1} -> {group} : {result1}")
    
# test_value2 = -1
# group = [1, 5, 8, 3]
# result2 = is_value_in_group(test_value2,group)
# print(f"{test_value2} -> {group} : {result2}")