print("Welcome to the Grade Sorter App")

#create list
grades=[]

#get user input
grade = int(input("\nEnter your first grade: "))
grades.append(grade)           
grade = int(input("Enter your next grade: "))
grades.append(grade)
grade = int(input("Enter your next grade: "))
grades.append(grade)
grade = int(input("Enter your last grade: "))
grades.append(grade)

#print and sort
print ("\nYour grades are: " + str(grades))

#sort
grades.sort(reverse = True)
print("Your grades from highest to lowest are: " + str(grades))

print("\nThe two lowest grades will now be dropped.")
grade1 = grades.pop()
grade2 = grades.pop()
print("Removed grade: " + str(grade1))
print("Removed grade: " + str(grade2))

print("\nYour remaining grades are: " + str(grades))

if grades[0] >=80:
    print("Nice work!  Your highest grade is " + str(grades[0]))
else:
    print("Tutors are available at the resource center.")


              
