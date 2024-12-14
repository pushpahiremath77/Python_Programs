import random

# UC7: Play the game with 2 players and report which player won the game
def play_two_players():
    position1 = 0
    position2 = 0
    rolls1 = rolls2 = 0
    winner = None
    
    while position1 != 100 and position2 != 100:
        # Player 1's turn
        rolls1 += 1
        dice_roll = random.randint(1, 6)
        option = random.randint(1, 3)
        
        if option == 1:  # No Play
            pass
        elif option == 2:  # Ladder
            position1 += dice_roll
        else:  # Snake
            position1 -= dice_roll
        
        if position1 < 0:
            position1 = 0
        if position1 > 100:
            position1 -= dice_roll
        
        if position1 == 100:
            winner = "Player 1"
            break
        
        # Player 2's turn
        rolls2 += 1
        dice_roll = random.randint(1, 6)
        option = random.randint(1, 3)
        
        if option == 1:  # No Play
            pass
        elif option == 2:  # Ladder
            position2 += dice_roll
        else:  # Snake
            position2 -= dice_roll
        
        if position2 < 0:
            position2 = 0
        if position2 > 100:
            position2 -= dice_roll
        
        if position2 == 100:
            winner = "Player 2"
            break
        
        # Reporting after each roll
        print(f"Player 1: Roll {rolls1}, Position: {position1}")
        print(f"Player 2: Roll {rolls2}, Position: {position2}")
    
    print(f"{winner} wins after {rolls1 + rolls2} rolls.")

play_two_players()
