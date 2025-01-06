def dice_roll(list1):
    total = 0
    for tupl in list1:
        if tupl[0] == tupl[1]:
            return 0
        total+=sum(tupl)
    return total

list1 = [(1, 1), (3, 4), (5, 6)]
result = dice_roll(list1)
print(result)