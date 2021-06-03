#print welcome statement
print("Welcome to the GPA Calculator App")

#get user input
name = input("What is your name? ").title()
userNum = int(input("How many grades would you like to enter? "))

#create and populate list
grades = []
for i in range(userNum):
    score = int(input("Enter grade: "))
    grades.append(score)

#Sort and print
grades.sort(reverse = True)


#Calculate average
avg = sum(grades)/len(grades)
avg = round(avg, 2)
#print summary
print("\n" + name + "'s Grade Summary: ")
print("\tTotal number of grades: " + str(userNum))
print("\tHighest grade: " + str(grades[0]))
print("\tLowest grade: " + str(grades[-1]))
print("\tAverage: " + str(avg))

#get user input for desired avg
desired = float(input("What is your desired average? "))
newScore = desired*(len(grades)+1) - sum(grades)
newScore = round(newScore, 2)
print("\nGood Luck " + name + "!\nYou will need to get a " + str(newScore) + " on your next assignment \nto earn a "
      + str(desired) + " average.")
#swap a grade
print("Let's see what your average would be if you did better or worse on an assignment: ")
swap = int(input("What grade would you like to change? "))
grades2 = grades[:]
newGrade = int(input("What grade would you like to change " + str(swap) + " to? "))
grades2.remove(swap)
grades2.append(newGrade)
grades2.sort(reverse = True)
newAvg = sum(grades2)/len(grades2)
newAvg = round(newAvg, 2)

#print new summary
print("\n" + name + "'s New Grade Summary: ")
print("\nYour grades from highest to lowest: ")
for score in grades2:
    print("\t" + str(score))
    
print("\n\tTotal number of grades: " + str(userNum))
print("\tHighest grade: " + str(grades2[0]))
print("\tLowest grade: " + str(grades2[-1]))
print("\tAverage: " + str(newAvg))
print("\nYour new average would be a " + str(newAvg) + " compared to your real average of " + str(avg))

change = newAvg - avg
change = round(change, 2)

print("That is a change of " + str(change) + " points !")
print("\nToo bad your original grades are still the same.")
print(str(grades))
print("You should go ask for extra credit!")
