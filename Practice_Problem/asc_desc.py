def asc_des(list1,string):
    if string == "Asc":
        list1.sort()
    elif string == "Des":
        list1.sort(reverse = True)
    return list1

list1 = [4,3,2,1]
string = "Des"
result = asc_des(list1,string)
print(result)