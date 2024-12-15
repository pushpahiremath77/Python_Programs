def split_list_based_on_first_char(words_list):

    result = {}
    for word in words_list:
        first_char = word[0].lower()
        if first_char not in result:
            result[first_char] = []
        result[first_char].append(word)
    return result

words_list = ['Apple', 'Banana', 'Avocado', 'Blueberry', 'Cherry', 'Carrot']
split_result = split_list_based_on_first_char(words_list)
for key, value in split_result.items():
    print(f"{key.upper()}: {value}")
