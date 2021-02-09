print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
# TODO: Write code to ask the client his savings and save it to another variable.
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
name = input("Hello what is your name?")
savings = input(f"Nice to meet you {name}, what is your savings today?")
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
print()

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.

'''
Your code should look like this:

if stock == "amzn":
    ...
elif ...
else ...
'''
num_of_stocks = 0
stock_choice = ''
if stock == "amzn":
    num_of_stocks = int(savings) / amazon
    stock_choice = 'amazon'
elif stock == "aaple":
    num_of_stocks = int(savings) / apple
    stock_choice = 'apple'
elif stock == "fb":
    num_of_stocks = int(savings) / fb
    stock_choice = 'fb'
elif stock == "goog":
    num_of_stocks = int(savings) / google
    stock_choice = 'google'
elif stock == "msft":
    num_of_stocks = int(savings) / msft
    stock_choice = 'msft'
else:
    num_of_stocks = f"Hey {name} we don't have those stock options"


print("Challenge 3.2.3: Output for the user the result")
# TODO: COnce you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

print(f"{name} has ${savings} in savings and he can buy {num_of_stocks} shares of {stock_choice} at the current price of $100")
