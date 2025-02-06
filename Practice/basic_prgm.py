# first = input("Enter first name:")
# last = input("Enter last name:")
# print(f"{first} {last}")

# number = (input("Enter numbers:"))
# numbers = number.split(",")

# my_tuple = tuple(numbers)
# my_list = list(numbers)


# print(f"{my_tuple}")
# print(f"{my_list}")

print("*******************")

# color_list = ["Red","Green","White" ,"Black"]
# print(f"First color: {color_list[0]} \nLast color:{color_list[-1]}")


tuple1 = (1,2,3,4,5,6,7)
element = 6
if element in tuple1:
    print("item exist")
else:
    print("item not exist")

reversed_tuple = tuple1[::-1]
print(reversed_tuple)

tuple2 = tuple1[2:5]
print(tuple2)

list1 = list(tuple1)
print(list1)

list1.remove(element)
print(list1)

my_tuple = tuple(list1)
print(my_tuple)


