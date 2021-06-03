#create list
userNames = ["hillg", "langa", "laettnerc", "tatumj", "hurleyb"]

#print welcome message
print("Welcome to the Shipping Accounts Program")

#get user input
user = input("\nWhat is your user name? ").lower().strip()
rate1 = "5.10"
rate2 = "5.00"
rate3 = "4.95"
rate4 = "4.80"

if user in userNames:
    print("\nWelcome, " + user + "!")
    print("\n\tCurrent shipping prices are as follows:")
    print("Shipping orders 0 to 100:\t\t$" + rate1 + " each")
    print("Shipping orders 100 to 500:\t\t$" + rate2 + " each")
    print("Shipping orders 500 to 1000:\t\t$" + rate3 + " each")
    print("Shipping orders over 1000:\t\t$" + rate4 + " each")
    
#get user input and calculate shipping          
    items = int(input("\nHow many items would you like to ship? "))
    if items <=100:
            price = items * 5.10
            price = round(price,2)
            print("To ship " + str(items) + " items will cost you $" + str(price) + " at $" + str(rate1) + " per item.")
    elif items <=500:
            price = items * 5.00
            price = round(price,2)
            print("To ship " + str(items) + " items will cost you $" + str(price) + " at $" + str(rate2) + " per item.")
    elif items <=1000:
            price = items * 4.95
            price = round(price,2)
            print("To ship " + str(items) + " items will cost you $" + str(price) + " at $" + str(rate3) + " per item.")
    else:
            price = items * 4.80
            price = round(price,2)
            print("To ship " + str(items) + " items will cost you $" + str(price) + " at $" + str(rate4) + " per item.")
    order = input("\nWould you like to place this order? (y/n): ").lower() 
    if order == "y":
            print("Okay.  Shipping your " + str(items) + " items.")
    else:
            print("Okay, no order is being placed at this time.")
            
else:
    print("Sorry, you do not have an account.  Goodbye.")
