def biggest_num(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
    

a=int(input("First number:"))
b=int(input("Second number:"))
c=int(input("Third number:"))

print(f"Biggest is: {biggest_num(a,b,c)}")