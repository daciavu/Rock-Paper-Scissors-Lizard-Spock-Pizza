import random
#create dictionary
thesaurus = {
    "Hot": ["arid", "balmy", "scorching", "blistering", "sizzling"],
    "Cold": ["icy", "frigid", "chilly", "freezing", "frosty"],
    "Happy": ["cheerful", "joyful", "jovial", "delighted", "merry"],
    "Sad": ["morose", "gloomy", "dejected", "despondent", "morose"],
    "Bright": ["shining", "dazzling", "vivid", "brilliant", "scintillating"],
    "Dark": ["dim", "gloomy", "murky", "dingy", "overcast"]
    }

#print welcome statement
print("Welcome to the Thesaurus app")
print("\nChoose a word in the thesaurus and I will give you a synonym.")
for key in thesaurus.keys():
    print("Here are the words in the thesaurus: -" + key)

#get user input
choice = input("\nWhat word would you like a synonym for? ").title().strip()
if choice in thesaurus.keys():
    index = random.randint(0,5)
    print("A synonym for " + choice + " is " + thesaurus[choice][index] + ".")
else:
    print("Sorry, that word is not in the thesaurus.")

#ask if user wants to see entire list
question= input("\nWould you like to see the whole thesaurus(yes/no)? ").lower().strip()
if question.startswith("y"):
    for key,values in thesaurus.items():
        print("\n" + key + " synonyms are: ")
        for value in values:
            print(value.title())
else:
    print("I hope you enjoyed the program.  Goodbye.")
