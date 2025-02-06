def count_repeated(strings):
    count = 0
    for string in strings:
        if len(string)>=2 and string[0]==string[-1]:
            count+=1
    return count


def sort_by_last(list):
    return sorted(list, key=lambda x: x[-1])


strings =  ['abc', 'xyz', 'aba', '1221', 'xyzyx']
print("Count of matching strings:",count_repeated(strings))

list =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] 
print("Sorted tuples:",sort_by_last(list))


print("***********************")
def remove_duplicates(items):
    return set(items)

items = [1, 2, 3, 2, 4, 5, 1, 6]
print("List after removing duplicates:", remove_duplicates(items))

def common_member(list1,list2):
    return any(item in list1 for item in list2)

list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]
print("Common items from 2 lists:",common_member(list1,list2))


def removed_word(list1):
    removed = []
    for i in range(len(list1)):
        if i not in [0, 4, 5]:
            removed.append(list1[i])
    return removed

list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("After removing words:",removed_word(list1))