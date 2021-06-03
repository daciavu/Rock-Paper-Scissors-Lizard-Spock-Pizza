import datetime
print("Welcome to the Grocery List App")

foods = ["Bacon", "Cheese"]

#print current date and time
time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)
print("Current Date and Time: " + month + "/" + day + " " + hour + ":" + minute)

#Get user input
print("\nYour list currently contains " )
print(foods [0],foods[1])
item = input("\nWhat would you like to add to your list? ").title()
foods.append(item)
item = input("What would you like to add to your list? ").title()
foods.append(item)
item = input("What would you like to add to your list? ").title()
foods.append(item)
print()
print(foods[0],foods[1],foods[2],foods[3],foods[4])
print("That is your current shopping list.")
foods.sort()
print("Your sorted list is: ")
print(foods[0],foods[1],foods[2],foods[3],foods[4])
print()

#Simulate shopping
print("\nCurrent grocery list: " + str(len(foods)) + " items")
print(foods[0],foods[1],foods[2],foods[3],foods[4])
item1 = input("\nWhat food did you just buy? ").title()
foods.remove(item1)
print("\nCurrent grocery list: " + str(len(foods)) + " items")
print(foods[0],foods[1],foods[2],foods[3])

item2 = input("What food did you just buy? ").title()
foods.remove(item2)
print("\nCurrent grocery list: " + str(len(foods)) + " items")
print(foods[0],foods[1],foods[2])

item3 = input("What food did you just buy? ").title()
foods.remove(item3)
print("\nCurrent grocery list: " + str(len(foods)) + " items")
print(foods[0],foods[1])

print("Sorry, the store is out of " + foods[1] + ".")
item4 = input("What would you like instead? ").title()

#replace item on list
item4 = foods[1]
foods.sort()
print("\nHere is what remains on your grocery list: ")
print(foods[0],foods[1])
