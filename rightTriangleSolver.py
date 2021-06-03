import math

#Print Welcome Message
print("Welcome to the Right Triangle Solver App")

#Get user input
sideA = float(input("What is the first leg of the triangle? "))
sideB = float(input("What is the second leg of the triangle? "))                   


#Calculate hypoteneuse
hypo = math.sqrt(sideA**2 + sideB**2)
hypo = round(hypo, 3)

#Calculate area
area = (sideA * sideB)/2
area = round(area, 3)


#Print Output
print("For a triangle with legs of " + str(sideA) + "and " + str(sideB) + "the hypoteneuse is " + str(hypo))
print("For this triangle the area is " + str(area))
