def rearrange_num(num):
    num = str(num)
    max_val = int(''.join(sorted(num,reverse=True)))
    min_val = int(''.join(sorted(num)))
    return max_val - min_val

num = 972882
result = rearrange_num(num)
print(result)
