#print welcome message
print("Welcome to the Yes or No Polling App")

#get user input
issue = input("\nWhat is the yes or no issue we will be voting on today? ").title()
numVote = int(input("How many people will be voting today? "))
passwd = input("What password will be used to view voting results? ")
#create dict
yes = 0
no = 0
results = {}
#polling loop
for i in range(numVote):
    name = input("\nPlease enter your full name: ").title().strip()
    if name in results.keys():
        print("Sorry, you have already voted.")
    else:
        print("Our issue is: " + issue + "?")
        vote = input("What is your vote? (yes/no) ").lower().strip()
        if vote =="y" or vote == "yes":
            vote = "yes"
            yes += 1
        elif vote == "n" or vote == "no":
            vote = "no"
            no += 1
        else:
            print("That is not a yes or no, but your vote will be recorded.")
            
#add results to dict
        results[name] = vote
        print("Thank you, " + name + " Your vote has been recorded.")
        
#display voting summary
print("\nThe total number of voters is: " + str(numVote))
for name, vote in results.items():
    print(name.title())

#display final voting result
print("\nOn the following issue, " + issue + " ?")
if yes > no:
    print("Yes wins! " + str(yes) + " votes to " + str(no) + ".")
elif no > yes:
    print("No wins! " + str(no) + " votes to " + str(yes) + ".")
else:
    print("It was a tie! " + str(yes) + "votes to " + str(no) + ".")
pw = input("\nTo see the results please enter the password: ")
if pw == passwd:
    for name, vote in results.items():
        print(name.title() + ":\t\t" + vote.title())
else:
    print("Sorry, that is not the correct password.")
print("Thank you for using the Yes or No Issue Polling App.")
