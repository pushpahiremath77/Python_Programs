# for i in range(100, 401):
#     temp = i 
#     while temp > 0:
#         digit = temp % 10  
#         if digit % 2 != 0:  
#             break  
#         temp = temp // 10  
#     else:
#         print(i, end=" ")


def find_even_digit_numbers():
    result = []
    for num in range(100, 401):  
        num_str = str(num)  
        
        if all(int(digit) % 2 == 0 for digit in num_str):
            result.append(num_str)  
    
    print(",".join(result))  


find_even_digit_numbers()
