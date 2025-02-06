class AgeError(Exception):
    pass

print(dir(Exception))
print("==>",Exception.__dict__)
ex1=AgeError("Inavlid Age")
print("\n Exception -->",ex1.__dict__,"\n")

age = int(input("Enter age:"))

try:
    if age >18:
        print("Valid")
    else:
        raise AgeError("Inavlid Age")
except:
    print("fcf")
    

