def first_before_second(txt, first, second):
    last_first = txt.rfind(first) 
    first_second = txt.find(second)  
    return last_first < first_second

print(first_before_second("a rabbit jumps joyfully", "a", "j"))