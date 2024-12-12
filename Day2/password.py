def validate_password(password):
    
    if len(password) < 6 or len(password) > 16:
        print("Password should have min-length 6 and max-length 16")
        return
        
    lower_count=0
    upper_count=0
    digit_count=0
    special_count=0


    for char in password:
        
        if char.isupper():
            upper_count+=1

        elif char.islower():
            lower_count+=1

        elif char.isdigit():
            digit_count+=1

        elif char in "$#@":
            special_count+=1

    if upper_count<1:
        print("It should have atleast one upper case")
        return
    
    if lower_count<2:
        print("It should have atleast two lower case")
        return
    
    if digit_count<1:
        print("It should have atleast one digit")
        return
    
    if special_count<1:
        print("It should have atleast one special character")
        return
    

    print("Valid password!!!")
    
password=input("Enter password:")
validate_password(password)




    