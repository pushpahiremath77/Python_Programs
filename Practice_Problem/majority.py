nums = [2,2,1,1,1,1,2]
new_dict = {}
for num in nums:
    if num not in new_dict:
        new_dict[num]=1
    else:
        new_dict[num]+=1
max_key = max(new_dict,key=new_dict.get)
print(max_key)
