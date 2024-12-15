def generate_square_dict(n):
    square_dict = {}
    for x in range(1, n + 1):
        square_dict[x] = x * x
    return square_dict

n = 6
result = generate_square_dict(n)
print(result)
