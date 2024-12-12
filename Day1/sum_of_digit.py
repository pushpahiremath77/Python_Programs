def sum_of_digit(n):
    sum = 0
    for i in str(n):
        sum=sum+int(i)
    print(f"Sum : {sum}")

n = int(input("Enter a number:"))
sum_of_digit(n)