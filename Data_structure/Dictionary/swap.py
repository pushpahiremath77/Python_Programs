def swap_dict(d):
    return {v: k for k, v in d.items()}

data = {'a': 1, 'b': 2, 'c': 3}
swapped = swap_dict(data)
print(swapped)
