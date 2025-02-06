def count_items_in_dict_values(dict_obj):
    total_count = 0
    for value in dict_obj.values():
        if isinstance(value, list):
            total_count += len(value)
    return total_count


sample_dict = {
    'fruits': ['apple', 'banana', 'cherry'],
    'vegetables': ['carrot', 'spinach'],
    'drinks': 'water',  
    'snacks': ['chips', 'cookies', 'nuts']
}

print("Total number of items in dictionary values that are lists:", count_items_in_dict_values(sample_dict))

print("***********************************")

def sum_of_list(items):
    return sum(items)

items = [1, 2, 3, 4, 5]
print("Sum of all items in list:", sum_of_list(items))


def multi_list(items):
    product = 1
    for item in items:
        product*=item
    return product

items = [1, 2, 3, 4, 5]
print("Product of all items in list:", multi_list(items))


def small(items): 
    return min(items)
items = [1, 2, 3, 4, 5]
print("Smallest  among all items in list:", small(items))

def large(items): 
    return max(items)
items = [1, 2, 3, 4, 5]
print("Largest  among all items in list:", large(items))



