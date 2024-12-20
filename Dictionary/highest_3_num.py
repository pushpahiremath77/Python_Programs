my_dict = {'a': 50, 'b': 200, 'c': 150, 'd': 400, 'e': 250, 'f': 100}

highest_3 = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True)[:3])

print("Top 3 highest values and corresponding keys:", highest_3)
