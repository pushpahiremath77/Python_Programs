def is_key_present(x):
    my_dict = {1:10,2:20,3:30,4:40}
    #for key in my_dict:
    if x in my_dict:
        print(f"Key {x} is present in dict") 
    else:
        print(f"Key {x} is not present in dict") 
    

is_key_present(6)