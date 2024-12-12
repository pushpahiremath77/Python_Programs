# n = int(input("Enter a number:"))
# # i=1
# # while(i<11):
# #     print(f"{n} * {i} = {n*i}")
# #     i+=1
# def table(n):
#     for i in range(1,11):
#         print(f"{n} * {i} = {n*i}")
#     print("\n")



# for i in range(1, n+1):
#     table(i)

# i=1
# while(i<10):
#     print(n*i)
#     i+=1


def create_table(n):
    i=1
    while i < 11:
        print(f"{n} * {i} = {n*i}")
        i+=1
    print("\n")

num = int(input("Enter a number"))
initial_table = 1

    # create_table(initial_table)
    # initial_table+=1

while initial_table < num+1:
    match initial_table:
        case 1:
            create_table(1)
    
        case 2:
            create_table(2)

        case 3:
            create_table(3)

        case 4:
            create_table(4)

        case 5:
            create_table(5)

        case _:
            print("nothing")
    initial_table += 1