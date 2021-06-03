#print welcome message
print("Welcome to the Temperature Conversion App")


#Get user input
Far = float(input("Enter the temperature in degrees Fahrenheit: "))


#Convert to Celsius
Cel = (5/9) *(Far - 32)
Cel = round(Cel,4)
                  
#Convert to Kelvin
Kel = Cel + 273.15
Kel = round(Kel,4)
Far = round(Far, 4)

#print results
print("Degrees Fahrenheit: \t" + str(Far))
print("Degrees Celsius: \t" + str(Cel))
print("Degrees Kelvin: \t" + str(Kel))
