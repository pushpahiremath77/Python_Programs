import random

def roll_die():
    return random.randint(1, 6)

def get_option():
    option = ['NO_PLAY', 'LADDER', 'SNAKE']
    return random.choice(option)
    
def uc3():
    position=0
    die=roll_die()
    choice=get_option()
    if choice=='LADDER':
        position+=die
        print(f"{choice}! The player move ahead to position {position}")
    elif choice=='SNAKE':
        position-=die
        if position<0:
            position=0
        print(f"{choice}! The player move behind to the position {position}")
    else:
        print(f"{choice}! The player stays in the same position")


uc3()