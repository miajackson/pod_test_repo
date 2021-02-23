
print('Question 1')
print()
# You're starting a deli and your supplier currently provides with these ingredients
meats = ['ham', 'turkey', 'chicken', 'tuna']
cheeses = ['cheddar', 'swiss', 'pepper jack', 'provolone']

# You want to create a menu soon, but first things first...
# TODO: Let's capitalize the first letter of each word in each list using .capitalize()


for i in range(len(meats)):
   meats[i] = meats[i].capitalize()

print(f'Here is an example of the first letter in the "meats" list capitalized: {meats}')

print()
print("&")
print()


for food in range(len(cheeses)):
    cheeses[food] = cheeses[food].capitalize()

print(f'Here is an example of the first letter in the "cheeses" list capitalized: {cheeses}')

print()

print('Question 2')
# Great! Your lists look much better. You need to come up with every combination of meats and cheeses for your menu.
# TODO: Use nested loops to create every combination of meat and cheese and add it to the sandwiches list
sandwiches = []

print("Here is the combination of meats and cheeses:")
print()
for meat in meats:
    for cheese in cheeses:
        sandwiches.append(f'{meat} & {cheese}')
print(sandwiches)

print()

print('Question 3')
# TODO: Let's create an input to take a customer order for a sandwich, for example: 'Ham & Swiss'

order = input(f' What type of sandwhich would you like? Please select from the following list: ')


print()

for sandwich in sandwiches:
    if order == sandwich:
        print(f'Your of {order} will be up shortly')


# TODO: Loop over the sandwiches list.
# TODO: If it exists, print 'Great choice! 1 Ham & Swiss coming right up!'