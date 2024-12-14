def find_largest_smallest(lst):
    largest = max(lst)
    smallest = min(lst)
    return largest, smallest

my_list = [3, 8, 1, 10, 15, 6]
largest, smallest = find_largest_smallest(my_list)
print(f"Largest: {largest}, Smallest: {smallest}")
