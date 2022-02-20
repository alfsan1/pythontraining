#using elif, else, if,
## checking balance of btc account and see if interest is applicable
## we will use int to parse the numbers

balance = input("how many btc do you currently hold ")

if int(balance) <= 2:
    print("Not applicable for extra interest earnings")
elif int(balance) <= 10 :
    print("Your balance of " + str(balance) + " is applicable for a 1% interest rate")
else:
    print("your balance of " + str(balance) + " will receive a 2.5% interest rate")
