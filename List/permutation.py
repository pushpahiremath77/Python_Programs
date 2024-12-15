import itertools

def generate_permutations(input_list):
    permutations = itertools.permutations(input_list)
    for perm in permutations:
        print(perm)
input_list = [1, 2, 3]

generate_permutations(input_list)





# def generate_permutations(input_list):

#     if len(input_list) == 0:
#         return [[]]
#     if len(input_list) == 1:
#         return [input_list]
#     permutations = []

#     for i in range(len(input_list)):
#         current_element = input_list[i]
#         remaining_elements = input_list[:i] + input_list[i+1:]

#         for perm in generate_permutations(remaining_elements):
#             permutations.append([current_element] + perm)
#     return permutations

# input_list = [1, 2, 3]
# permutations = generate_permutations(input_list)
# for perm in permutations:
#     print(perm)
