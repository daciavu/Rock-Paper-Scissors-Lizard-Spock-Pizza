
print("Welcome to the Miles per Hour Conversion App!")

#Get user input
speed = float(input("\nWhat is your speed in miles per hour? "))

#Convert to mps
speed = speed * 0.4474
mps = round(speed,2)

#print converted vaue
print("Your speed in meters per second is: " +  str(mps))
