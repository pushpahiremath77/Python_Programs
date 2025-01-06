nums = [4,1,4,3,2,1,2]
new_dict = {}
for item in nums:
    if item in new_dict:
        new_dict[item]+=1
    else:
        new_dict[item] = 1
for key,value in new_dict.items():
    if value==1:
        print(key)





def single_value(num):
    result = 0
    for num in nums:
        result ^= num
    return result
nums = [4,1,4,3,2,1,2]
result = single_value(nums)
print(result)