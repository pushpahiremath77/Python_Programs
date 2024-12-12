human_years=int(input("Enter dog's age in human years:"))
if human_years<=2:
    dog_age=human_years*10.5
elif human_years==0:
    print("Invalid age")
else:
    dog_age=(2*10.5)+(human_years-2)*4
print(dog_age)