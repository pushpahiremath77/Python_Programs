n = int(input("Enter a number:"))
is_perfect = False
for i in range(1,n+1):
    if i*i == n:
        is_perfect = True
        break

if is_perfect:
    print("Perfect square")
else:
    print("Not perfect square")







    