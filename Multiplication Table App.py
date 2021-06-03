print("Welcome to the Multiplication/Exponent Table App")
print()
#Get user input
name = input("What is your name? ").title().strip()
number = float(input("Please enter a number: "))


#Create multiplication table

ans1 = number * 1
ans1 = round(ans1, 4)
ans2 = number * 2
ans2 = round(ans2, 4)
ans3 = number * 3
ans3 = round(ans3, 4)
ans4 = number * 4
ans4 = round(ans4, 4)
ans5 = number * 5
ans5 = round(ans5, 4)
ans6 = number * 6
ans6 = round(ans6, 4)
ans7 = number * 7
ans7 = round(ans7, 4)
ans8 = number * 8
ans8 = round(ans8, 4)
ans9 = number * 9
ans9 = round(ans9, 4)


#print table
print()
print("Multiplication Table for " + str(number))
print()
print(str(number) + " * 1 = " + str(ans1))
print(str(number) + " * 2 = " + str(ans2))    
print(str(number) + " * 3 = " + str(ans3))
print(str(number) + " * 4 = " + str(ans4))
print(str(number) + " * 5 = " + str(ans5))
print(str(number) + " * 6 = " + str(ans6))
print(str(number) + " * 7 = " + str(ans7))
print(str(number) + " * 8 = " + str(ans8))
print(str(number) + " * 9 = " + str(ans9))
print()

#Create exponent table

exp1 = number**1
exp1 = round(exp1, 4)
exp2 = number**2
exp2 = round(exp2, 4)
exp3 = number**3
exp3 = round(exp3, 4)
exp4 = number**4
exp4 = round(exp4, 4)
exp5 = number**5
exp5 = round(exp5, 4)
exp6 = number**6
exp6 = round(exp6, 4)
exp7 = number**7
exp7 = round(exp7, 4)
exp8 = number**8
exp8 = round(exp8, 4)
exp9 = number**9
exp9 = round(exp9, 4)

#print table
print("Exponent Table for " + str(number))
print()
print(str(number) + "**1 = " + str(exp1))
print(str(number) + "**2 = " + str(exp2))
print(str(number) + "**3 = " + str(exp3))
print(str(number) + "**4 = " + str(exp4))
print(str(number) + "**5 = " + str(exp5))
print(str(number) + "**6 = " + str(exp6))
print(str(number) + "**7 = " + str(exp7))
print(str(number) + "**8 = " + str(exp8))
print(str(number) + "**9 = " + str(exp9))


#print message
message = name + " Math is cool!"
print()
print(message)
print("\t " + message.lower())
print("\t\t "+ message.title())
print("\t\t\t "+ message.upper())

