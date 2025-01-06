def odd_even_position(list1,string):
    new = []
    for i in range(len(list1)):
        if i%2!=0:
            new.append(list1[i])
    return new

list1 = [2, 4, 6, 8, 10]
string = "odd"
result = odd_even_position(list1,string)
print(result)