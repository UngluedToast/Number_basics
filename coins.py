

Want_coin = True 
coin_amount = 0 
while Want_coin:

    Querry = input("you have %s coins \n Do you want another?   " % (coin_amount))
    if Querry == "yes":
        coin_amount = coin_amount +1 
    elif Querry == "no":
        Want_coin = False
print("ok, bu-bye now!")












#prompt the user for another coin
    # yes or no
    # if yes print out total of coins + 1, repeat process
    # if no, stop the process