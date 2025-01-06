def run_length_encoding(input_string):
    result = ""
    count = 1
    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            result += str(count) + input_string[i - 1]
            count = 1 
    result += str(count) + input_string[-1]
    return result

input_string = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
encoded_string = run_length_encoding(input_string)
print("Encoded Output:", encoded_string)

#'12W1B12W3B24W1B14W'
