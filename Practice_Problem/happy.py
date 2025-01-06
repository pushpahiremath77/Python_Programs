num =19
total =0
while num>9:
    while num>0:
        digit = num % 10
        total+=digit*digit
        num = num//10
    num = total
    total = 0

if num ==1:
    print("Happy num")
else:
    print("Not happy num")





