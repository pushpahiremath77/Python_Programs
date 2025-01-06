nums = [2, 3, 5, 7, 9]
target = 7

def find_target(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
    else:
        return -1

result = find_target(nums,target)
print(result)