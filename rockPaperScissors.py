import random

#print welcome statement
print("Welcome to a game of Rock,Paper,Scissors,Lizard,Spock,Pizza!")
userNum = int(input("\nHow many rounds would you like to play? " ))

#build list/setup
moves = ["Rock", "Paper","Scissors","Lizard","Spock","Pizza"]
score = 0
compScore = 0

for rounds in range(userNum):
    print("\nRound" + str(rounds + 1))
    print("\nPlayer: " + str(score) + "\tComputer: " + str(compScore))
    choice = input("Time to pick...Rock, Paper, Scissors, Lizard, Spock,Pizza: ").title().strip()
    compChoice = random.choice(moves)
    if choice in moves:    
        print("\nYou chose: " + choice + " I chose: " + compChoice + ":")
    
#paper
        if choice == compChoice:
            print("It's a tie!  How boring!")
            winner = "tie"
        elif choice == "Paper" and compChoice == "Rock":
            print("Paper covers Rock!  You win!")
            winner = "player"
        elif choice == "Paper" and compChoice == "Scissors":
            print("Scissors cut Paper!  You lose!")
            winner = "computer"
        elif choice == "Paper" and compChoice == "Lizard":
            print("Lizard eats Paper!  You lose!")
            winner = "computer"
        elif choice == "Paper" and compChoice == "Spock": 
            print("Paper disproves Spock!  You win!")
            winner = "player"
        elif choice == "Paper" and compChoice == "Pizza": 
            print("Pizza ruins Paper!  You lose!")
            winner = "computer" 
#rock            
        
        elif choice == "Rock" and compChoice == "Paper":
            print("Paper covers Rock!  You lose!")
            winner = "computer"
        elif choice == "Rock" and compChoice == "Scissors":
            print("Rock crushes Scissors!  You win!")
            winner = "player"
        elif choice == "Rock" and compChoice == "Lizard":
            print("Rock crushes Lizard!  You win!")
            winner = "player"
        elif choice == "Rock" and compChoice == "Spock": 
            print("Spock vaporizes rock!  You lose!")
            winner = "computer"
        elif choice == "Rock" and compChoice == "Pizza": 
            print("Rock smashes Pizza!  You win!")
            winner = "player" 

#scissors
        elif choice == "Scissors"and compChoice == "Paper":
            print("Scissors cut Paper!  You win!")
            winner = "player"
        elif choice == "Scissors" and compChoice == "Rock":
            print("Rock crushes Scissors!  You lose!")
            winner = "computer"
        elif choice == "Scissors" and compChoice == "Lizard":
            print("Scissors decapitate Lizard!  You win!")
            winner = "player"
        elif choice == "Scissors" and compChoice == "Spock": 
            print("Spock smashes Scissors!  You lose!")
            winner = "computer"
        elif choice == "Scissors" and compChoice == "Pizza": 
            print("Scissors cut Pizza!  You lose!")
            winner = "player" 

#lizard
        elif choice == "Lizard" and compChoice == "Paper":
            print("Lizard eats Paper!  You win!")
            winner = "player"
        elif choice == "Lizard" and compChoice == "Rock":
            print("Rock crushes Lizard!  You lose!")
            winner = "computer"
        elif choice == "Lizard" and compChoice == "Scissors":
            print("Scissors decapitate Lizard!  You lose!")
            winner = "computer"
        elif choice == "Lizard" and compChoice == "Spock": 
            print("Lizard poisons Spock!  You win!")
            winner = "player"
        elif choice == "Lizard" and compChoice == "Pizza": 
            print("Lizard tramples Pizza!  You win!")
            winner = "player" 

#Spock
        elif choice == "Spock" and compChoice == "Paper":
            print("Paper disproves Spock!  You lose!")
            winner = "computer"
        elif choice == "Spock" and compChoice == "Rock":
            print("Spock vaporizes Rock!  You win!")
            winner = "player"
        elif choice == "Spock" and compChoice == "Scissors":
            print("Spock smashes scissors!  You win!")
            winner = "player"
        elif choice == "Spock" and compChoice == "Lizard": 
            print("Lizard poisons Spock!  You lose!")
            winner = "computer"
        elif choice == "Spock" and compChoice == "Pizza": 
            print("Pizza burns Spock!  You lose!")
            winner = "computer"    

#Pizza
        elif choice == "Pizza" and compChoice == "Paper":
            print("Pizza ruins paper!  You win!")
            winner = "player"
        elif choice == "Pizza" and compChoice == "Rock":
            print("Rock smashes Pizza!  You lose!")
            winner = "computer"
        elif choice == "Pizza" and compChoice == "Scissors":
            print("Scissors cut pizza!  You lose!")
            winner = "computer"
        elif choice == "Pizza" and compChoice == "Lizard": 
            print("Lizard tramples Pizza!  You lose!")
            winner = "computer"
        elif choice == "Pizza" and compChoice == "Spock": 
            print("Pizza burns Spock!  You win!")
            winner = "player" 

        else:
            print("Winner not calculated.")
            winner = "tie"

#calculate scores        
        if winner == "player":
            score += 1
        elif winner == "computer":
            compScore += 1
        else:
            print("This round was a tie.")
    else:
        print("Not a valid game option.")
        compScore = compScore + 1
             
#Output final results
print("\nFinal Game Results: ")
print("Rounds Played : " + str(userNum ))
print("Player Score: " + str(score))
print("Computer Score: " + str(compScore))
if score > compScore:
    print("Winner: Player :)")
elif score < compScore:
    print("Winner: Computer :-(")
else:
    print("Winner: None--it's a tie.")
