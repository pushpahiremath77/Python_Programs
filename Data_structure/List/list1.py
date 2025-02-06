def sum_of_items(list1):
    sum = 0
    # for item in list1:
    #     sum+=item
    # return sum

    for i in range(len(list1)):
        sum+=list1[i]
    return sum

list1 = [1,2,3,4,5]
sum = sum_of_items(list1)
print(f"Sum:{sum}")


def product_of_items(list1):
    product = 1
    for item in list1:
        product*=item
    return product

list2 = [1,2,3,4,5]
product = product_of_items(list2)
print(f"Product:{product}")


def smallest(list1):
    smallest = float('inf')
    s_smallest = float('inf')
    for item in list1:
        if item < smallest:
            s_smallest = smallest
            smallest = item
    return s_smallest

list2 = [45,65,73,13]
s_smallest = smallest(list2)
print(f"Second smallest:{s_smallest}")



def count_string(list3):
    count = 0
    for string in list3:
        if len(string)>=2 and string[0] == string[-1]:
            count+=1
    return count

list3 = ['abc', 'xyz', 'aba', '1221','psp'] 
count = count_string(list3)
print(f"Number of string has same char in first and last:{count}")

def get_last_element(item):
    return item[-1]

def sort_tuples(list1):
    return sorted(list1, key=get_last_element)

list4 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] 
sorted_list = sort_tuples(list4)
print(sorted_list)



def remove_duplicates(list1):
    removed = []
    for item in list1:
        if item not in removed:
            removed.append(item)
    return removed

list5 = [1,2,4,1,5,3,4,1]
removed = remove_duplicates(list5)
print(removed)



def longer_word(list1):
    result = []
    n=3
    for item in list1:
        if len(item)>n:
            result.append(item)
    return result

list6 = ['python','list','abc','ab']
longer_words = longer_word(list6)
print(longer_words)



def copy_list(list1):
    copy_list1 = list1.copy()
    return copy_list1

list7 = [1,2,3,4,5]
copy_list1 = copy_list(list7)
print(f"Original list:{list7}")
print(f"Copied list :{copy_list1}")





def common_member(list1,list2):
    # for item in list1:
    #     if item in list2:
    #         return True
    # return False
    return set(list1) & set(list2)
        
list8 = [1,2,3,4,5]
list9 = [6,7,8,3,4]
print(common_member(list8,list9))



def remove_element(list1):
    new_list = []
    for i in range(len(list1)):
        if i not in [0,4,5]:
            new_list.append(list1[i])
    return new_list
color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] 
removed_list = remove_element(color_list)
print(removed_list)



import itertools
def generate_permutations(list1):
    permutations = itertools.permutations(list1)
    for item in permutations:
        print(item)

list_perm = [1,2,3]
generate_permutations(list_perm)




def difference_lists(list1,list2):
    # return set(list1) - set(list2)
    new_list = []
    for item in list_1:
        if item not in list_2:
            new_list.append(item)
    return new_list

list_1 = [1,2,3,4,5]
list_2 = [5,6,7,8]
difference = difference_lists(list_1,list_2)
print(f"Difference:{difference}") 



def append_list(list1,list2):
    return list1 + list2

list_3 = [1,2,3,4,5]
list_4 = [5,6,7,8]
appended_list = append_list(list_3,list_4)
print(f"Appended list:{appended_list}")


def circularly_identical(list1,list2):
    concate_list = list1 + list1
    for i in range(len(list1)):
        if concate_list[i:i+len(list2)] == list2:
            return True
    return False

list_5 = [1,2,3,4]
list_6 = [3,4,1,2]
print(circularly_identical(list_5,list_6))


def common_items(list1,list2):
    new_list = []
    for item in list1:
        if item in list2:
            new_list.append(item)
    return new_list

list11 = [1,2,3,4,5]
list22 = [4,5,6,3,7,8]
print(common_items(list11,list22))



def split_list(list1):
    new_dict = {}
    for word in list1:
        f_char = word[0]
        if f_char not in new_dict:
            new_dict[f_char] = []
        new_dict[f_char].append(word)
    return new_dict

new_list = ["Pushpa","Pooja","Disha","Viju","Pram"]
dict1 = split_list(new_list)
print(dict1)

def remove_duplicated(list1):
    new_list = []
    for item in list1:
        if item not in new_list:
            new_list.append(item)
    return new_list

rm_list =[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]] 
count1 = rm_list.count([30,56,25])
print(f"count = {count1}")
print(f"Index = {rm_list.index([40])}")
removed_dup = remove_duplicates(rm_list)
print(removed_dup)
print(f"After popped :{rm_list.pop(4)}")




def armstrong_num(num):
    number = str(num)
    length = len(number)
    sum = 0
    for item in number:
        sum+=int(item) ** length
    return sum == number

num = int(input("Enter a number:"))
if armstrong_num(num):
    print(f"{num} is armstrong number")
else:
    print(f"{num} is not armstrong number")

