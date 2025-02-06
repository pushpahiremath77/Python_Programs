def decorator_fun(hello):
    def modify():
        print("Good morning")
        hello()
    return modify

@decorator_fun
def hello():
    print("Hello wrd")
    
hello()