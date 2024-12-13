def school_trip():
    students=int(input("Enter number of students:"))

    if students<250 or students>351:
        print("Number of students should be between 250 & 350")
        return
    
    teachers=int(input("Enter number of teachers:"))

    participants=students+teachers
    print(f"Total number of participants:{participants}")

    large_bus=participants//46
    print(f"Number of large buses are: {large_bus}")
    remained_large=participants%46

    small_bus=remained_large//16
    remained_small=remained_large%16

    if remained_small>1:
        small_bus=small_bus+1   
    print(f"Number of small buses:{small_bus}")
    
    total_cost=large_bus*360 + small_bus*140
    print(f"Total cost needs for hiring coaches:{total_cost}")

school_trip()