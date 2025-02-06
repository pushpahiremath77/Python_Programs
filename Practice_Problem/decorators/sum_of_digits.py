def decorate_sum(func):
    def sum_of_digit(n):
        sum=0
        n = func(n)
        while(n>0):
            remainder = n%10
            sum+=remainder
            n=n//10
        print(sum)
    return sum_of_digit

@decorate_sum
def sum_digit(n):
    return n
    

sum_digit(12345)