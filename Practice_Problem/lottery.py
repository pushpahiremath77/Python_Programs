def lottery_ticket(ticket,win):
    mini_wins = 0
    for sublist in ticket:
        string,number = sublist
        if any(ord(char)==number for char in string):
            mini_wins+=1
        print(mini_wins)
    return "Winner!" if mini_wins >= win else "Loser!"

ticket = [["KG", 80],["IJK",73], ["NTBBVZ", 79], ["CI", 73], ["AGXMEE", 74], ["IU", 68], ["VOSP" , 84]]
win = 2
result = lottery_ticket(ticket,win)
print(result)