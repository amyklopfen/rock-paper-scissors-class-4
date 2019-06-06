import random

def my_message():
    return "Hello"

x = my_message()
print(x)

#only if this code is executed from the command line
if __name__ == "__main__":
    
    #capture inputs 
    print("welcome to rock, paper, scissors, shoot.")
    user_input = input("please choose one of the following options: rock, paper, or scissors ")
    x = user_input

    game_list = ["rock","paper","scissors"]

    computer = random.choice(game_list)

    #generate computer inputs
    print("you chose", x)
    print("computer chose", computer)

    #validate inputs
    if x not in game_list:
        print("error, invalid entry. enter rock, paper, or scissors")
        exit()   

    #determine the winner
    if x == computer: #== compares user choice to computer choice; not assigning value to a variable
        print("it's a tie")
    elif x == "rock" and computer == "paper":
        print("you lose!")
    elif x == "rock" and computer == "scissors":
        print("you win!")
    elif x == "paper" and computer == "scissors":
        print("you lose!")
    elif x == "paper" and computer == "rock":
        print("you win!")
    elif x == "scissors" and computer == "rock":
        print("you win!")
    elif x == "scissors" and computer == "paper":
        print("you win!")#display the final outputs/outcomes

    print("thanks for playing!")


