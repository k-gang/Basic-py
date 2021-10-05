import random

comp_wins = 0
player_wins = 0

def user_option():
    user_choice = input("Choose Rock, Paper or Scissors: ")
    if user_choice in ["Rock", "rock", "r", "R"]:
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "p", "P"]:
        user_choice = "p"
    elif user_choice in ["Scissors", "scissors", "s", "S"]:
        user_choice = "s"
    else:
        print("wrong input,try again mate")
        user_option()
    return user_choice

def pc_option():
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice


while True:
    print("")
    
    user_choice = user_option()
    comp_choice = pc_option()

    print("")
    
    if user_choice == "r":
        if comp_choice == "r":
            print("tie! both of u chose rock")
        
        elif comp_choice == "p":
            print("u lost! Ai chose paper and u chose rock")
            comp_wins += 1
            
        elif comp_choice == "s":
            print("u won! Ai chose scissor and u chose rock")
            player_wins += 1

    elif user_choice == "p":
        if comp_choice == "r":
            print("u win!. Ai chose rock and u chose paper")
            player_wins += 1
        
        elif comp_choice == "p":
            print("tie! both of u chose paper")
            
            
        elif comp_choice == "s":
            print("u lose! Ai chose scissor and u chose paper")
            comp_wins += 1

    elif user_choice == "s":
        if comp_choice == "r":
            print("u lose! Ai chose rock and u chose scissor")
            comp_wins += 1
        
        elif comp_choice == "p":
            print("u win!. Ai chose paper and u chose scissor")
            player_wins += 1
            
        elif comp_choice == "s":
            print("tie! both of u chose scissor")

    print("")
    print("Player wins: " + str(player_wins))
    print("Computer wins: " + str(comp_wins))
    print("")
    
    user_choice = input("Do you want to play again? (y/n)")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N", "n", "no", "No"]:
        break
    else:
        break