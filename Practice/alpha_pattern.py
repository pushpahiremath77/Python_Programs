n=5
for i in range(1,n+1):
    for j in range(i):
        print(chr(64+i),end=" ")
    print()

for i in range(n-1,0,-1):
    for j in range(i):
        print(chr(64+i),end=" ")
    print()
