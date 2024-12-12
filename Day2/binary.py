
binary_nums = input("Enter binary numbers: ").split(',')


for binary in binary_nums:
    decimal_num = int(binary, 2)  
    if decimal_num % 5 == 0:     
        print(f"{binary} is divisible by 5")
