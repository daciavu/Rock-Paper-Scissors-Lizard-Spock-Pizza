import random

#print welcome statement
print("Welcome to the Coin Toss App.")

#get user input
userNum = int(input("How many times would you like to flip the coin? "))
choice = input("Would you like to see the result of each coin flip? ").lower()
if choice.startswith('y'):
    choice = True

#create heads/tails variables
heads = 0
tails = 0

#flip coin
for i in range(1, userNum):
    flip = random.randint(0,1)
    if flip == 0:
        heads = heads + 1
        if choice == True:
            print("heads = " + str(heads) + " tails = " + str(tails))
        if heads == tails:
            print("The coin has flipped heads and tails the same number of times.")
    else:
        tails = tails + 1
        if choice == True:
            print("heads = " + str(heads) + " tails = " + str(tails)) 
        if heads == tails:
            print("The coin has flipped heads and tails the same number of times.")

#Calculate and display percentages
headsPercent = (heads/userNum)*100
headsPercent = round(headsPercent,2)
tailsPercent = (tails/userNum)*100
tailsPercent = round(tailsPercent, 2)
print("\nHeads was flipped " + str(heads) + " times, which is " + str(headsPercent) + "%.")
print("Tails was flipped " + str(tails) + " times, which is " + str(tailsPercent) + "%.")
