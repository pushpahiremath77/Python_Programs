import random

def guess_number():
    random_num=random.randint(1,9)
    guess_num=0
    while(random_num!=guess_num):
        guess_num = int(input("Guess the number between 1 and 9: "))
        if random_num != guess_num:
            guess_num=int(input("Wrong guess.....Guess the number again:"))
    print("Well guessed!!!")
 

guess_number()


