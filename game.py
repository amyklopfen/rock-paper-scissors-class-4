import random

#capture inputs 
print("welcome to rock, paper, scissors, shoot.")
user_input = input("please choose one of the following options: rock, paper, or scissors")
x = user_input

game_list = ["rock","paper","scissors"]

computer = random.choice(game_list)
#validate inputs

"rock" > "scissors"
"scissors" > "paper"
"paper" > "rock"

#generate computer inputs
print("you chose", x)
print("computer chose", computer)

#determine the winner
if x not in game_list:
    print("error, invalid entry. enter rock, paper, or scissors")
    exit()   

if x == computer:
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
    print("you win!")
#display the final outputs/outcomes


