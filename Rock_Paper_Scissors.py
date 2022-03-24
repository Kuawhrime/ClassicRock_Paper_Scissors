import random

player_win = 0
bot_win = 0

# Les possibilité de notre jeu dans une liste 
choice = ["rock", "paper", "scissors"]

# Les boucles que nous allons effectuer avec une demande et les possibilités énoncé
while True:
    choices = input("Make a choice \ rock | paper | scissors / but if the choice is the letter q the party is ending : ")
    if choices == "q":
        break
        
    if choices not in choice:
        continue

# Le choix au hazard du bot
    random_nbr = random.randint(0, 2)
    bot_choice = choice[random_nbr]
    print("The bot choice", bot_choice + ".")

# La conditions pour mettre les règles au préalable pour chaque choix

#Les règles établit part des conditions

    if choices == "rock" and bot_choice == "scissors":
        print("You won this party")
        player_win += 1
    
    elif choices == "paper" and bot_choice == "rock":
        print("You won this party")
        player_win += 1

    elif choices == "scissors" and bot_choice == "paper":
        print("You won this party")
        player_win += 1

    else:
        print("The bot won this party")
        bot_win += 1



# La fin du programme par l'énonciation des nombres de partie
print("The number of game win by the player is ", player_win, "games")
print("The number of game win by the bot is ", bot_win, "games")

print("Fin du Jeu")
