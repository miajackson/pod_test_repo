#print("Challenge 3.2: Playing with the stock market")


# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

#print("Challenge 3.2.1: Taking user input")
print("Welcome")
name = input("What is your name?")
savings = int(input("How much savings do you have ?"))
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google, 'msft' for Microsoft.")


#print("Challenge 3.2.2: Perform user-specific calculations")

company_stock = 1

if stock == "amzn":
    price = amazon
    company_stock = savings/price
elif stock == "aapl":
    price = apple
    company_stock = savings/price
elif stock == "fb":
    price = fb
    company_stock = savings/price
elif stock == "goog":
    price = google
    company_stock = savings/price
elif stock == "msft":
    price = msft
    company_stock = savings/price

#print("Challenge 3.2.3: Output for the user the result")
# TODO: COnce you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.
if price == "0":
    print("Stock not available")
else:
    print(f"{name} has ${savings} in savings and he can buy {company_stock} shares of {stock} at the current price of ${price}.")



