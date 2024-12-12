for i in range(100, 401):
    temp = i 
    while temp > 0:
        digit = temp % 10  
        if digit % 2 != 0:  
            break  
        temp = temp // 10  
    else:
        print(i, end=" ")

