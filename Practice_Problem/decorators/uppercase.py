def convert_case(func):
    def uppercase(name):
        result = str(func(name)).upper()
        print(result)
    return uppercase
        
@convert_case
def firstname(fname):
    return f"{fname}"
firstname("pushpa")

@convert_case
def lastname(lname):
    return f"{lname}"
lastname("hiremath")