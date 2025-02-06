num = [1,2,3,4,5]
square = list(map(lambda x:x**2,num))
print(square)



num = [1,2,3,4,5]
even = list(filter(lambda x:x%2==0,num))
print(even)

from functools import reduce
num = [1,2,3,4,5]
sum = reduce(lambda x,y:x+y,num)
print(sum)