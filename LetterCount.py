print("Welcome to the Letter Counting App!")

#Get user input

name = input("\n What is your name?").strip().title()
print("\n Hello, " + name + ".  This app will count the number of times a specific letter appears in a message.")

#Get message
message = input("Please enter a message: ").strip()
print("\n" +  message)

#Get user input
choice = input("What letter would you like me to count? ").strip().lower()

#counter
number = message.count(choice)

print("\n" + name + " Your message has " + str(number) + " " + choice + " 's in it.")
