#Print welcome message
print("Welcome to the Fibonacci Calculator App")

#Get User Input
userNum = int(input("\nHow many digits of the Fibonacci Sequence would you like to compute? "))

#create list and loop
fibList = [1,1]
for i in range(userNum - 2):
    newFibList = fibList[i] + fibList[i + 1]
    fibList.append(newFibList)

#display results
print("The first " + str(userNum) + "numbers of the Fibonacci sequence are: ")
print(fibList)

#calculate Golden Ratio values
Ratio = []
for i in range(len(fibList) - 1):
   fibList2 = fibList[i + 1]/fibList[i]
   Ratio.append(fibList2)

#Display results
print("\nThe corresponding Golden Ration values are: ")
for fibList2 in Ratio:
    print(fibList2)
print("\nThe ration of consecutive Fibonacci terms approaches Phi; 1.618...")
