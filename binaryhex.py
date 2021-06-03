print("Welcome to the Binary Hexadecimal Converter App")

#Get first user input
num1 = int(input("Compute binary and hexadecimal values up to the following decimal number: "))


#create lists
userNum = list(range(1, num1))
binary = []
hexadec = []
for i in range(len(userNum)):
    x = bin(userNum[i])
    binary.append(x)
    y = hex(userNum[i])
    hexadec.append(y)
print("Generating lists....complete!")

#Get user input for slicing
print("\nUsing slices, we will now show a portion of each list.")
startNum = int(input("What decimal would you like to start at? "))
endNum = int(input("What decimal would you like to stop at? "))
print("Decimal values from " + str(startNum) + " to " + str(endNum) + ": ")

#print slices
for num in userNum[startNum -1 : endNum]:
    print(num)
    
print("Binary values from " + str(startNum) + " to " + str(endNum) + ": ")
for num in binary[startNum - 1 : endNum]:
    print(num)

print("Hexadecimal values from " + str(startNum) + " to " + str(endNum) + ": ")
for num in hexadec[startNum - 1 : endNum]:
    print(num)

#print all
    
input("\nPress Enter to see all values from 1 to "  + str(userNum[-1]) + ".")
print("Decimal---Binary---Hexadecimal")
print("-------------------------------------")

for num in zip(userNum, binary, hexadec):
    print(str(num))
