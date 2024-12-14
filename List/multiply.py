def multiply_list(list):
    product = 1
    for num in list:
        product *= num
    return product

my_list = [1, 2, 3, 4]
print("Product of all elements:", multiply_list(my_list))
