from collections import Counter
#print welcome message and create list
print("Welcome to the Frequency Analysis App")

nonLetters = {",",".",";",":","!","#","\n","\t","$","%","&","*","~"," ","?","/","(",")","@","`","-",
    }

#get user input
phrase = input("Please enter a phrase to be analyzed: ").lower().strip()
#remove nonLetters
for nonLetter in nonLetters:
    phrase = phrase.replace(nonLetter, '')

#store remaining characters
totalOccurrences = len(phrase)

#setup counter
letterCount = Counter(phrase)

#print frequency analysis for phrase
print("\nHere is the frequency analysis for your phrase: ")
print("\n\tLetter\t\Occurrence\tPercentage")
for key, value in sorted(letterCount.items()):
    percentage = 100*value/totalOccurrences
    percentage = round(percentage, 2)
    print("\t" + key + "\t\t" + str(value) + "\t\t" + str(percentage) + "%")

#Sort list of letters from highest occurrence to lowest
orderedCount = letterCount.most_common()
phraseOrderedLetters = []
for pair in orderedCount:
    phraseOrderedLetters.append(pair[0])

print("\nLetters ordered from highest to lowest: ")
for letter in phraseOrderedLetters:
    print(letter, end="")

#get user input
phrase2 = input("\nPlease enter a phrase to be analyzed: ").lower().strip()
#remove nonLetters
for nonLetter in nonLetters:
    phrase2 = phrase2.replace(nonLetter, '')

#store remaining characters
totalOccurrences = len(phrase2)

#setup counter
letterCount = Counter(phrase2)

#print frequency analysis for phrase
print("\nHere is the frequency analysis for your phrase: ")
print("\n\tLetter\t\Occurrence\tPercentage")
for key, value in sorted(letterCount.items()):
    percentage = 100*value/totalOccurrences
    percentage = round(percentage, 2)
    print("\t" + key + "\t\t" + str(value) + "\t\t" + str(percentage) + "%")

#Sort list of letters from highest occurrence to lowest
orderedCount = letterCount.most_common()
phraseOrderedLetters = []
for pair in orderedCount:
    phraseOrderedLetters.append(pair[0])

print("\nLetters ordered from highest to lowest: ")
for letter in phraseOrderedLetters:
    print(letter, end="")
