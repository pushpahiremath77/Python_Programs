def table_decorator(func):
    def print_table(n):
        for i in range(1,11):
            print(f"{func(n)*i}")
    return print_table

@table_decorator
def table_num(n):
    return n

table_num(3)