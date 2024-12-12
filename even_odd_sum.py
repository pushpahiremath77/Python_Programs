even_sum=0
odd_sum=0
for i in range(1,11):
    if i%2==0:
        even_sum+=i
    else:
        odd_sum+=i
print("Even sum:",even_sum)
print("Odd sum:",odd_sum)
