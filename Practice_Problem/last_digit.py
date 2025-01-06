def last_dig(a, b, c):
    last_a = abs(a)%10
    last_b = abs(b)%10
    last_c = abs(c)%10

    last_product = (last_a*last_b)%10

    return last_product == last_c

print(last_dig(25, 21, 125))
