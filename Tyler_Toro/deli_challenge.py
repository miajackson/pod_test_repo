
print('Question 1')
# You're starting a deli and your supplier currently provides with these ingredients
meats = ['ham', 'turkey', 'chicken', 'tuna']
cheeses = ['cheddar', 'swiss', 'pepper jack', 'provolone']

# You want to create a menu soon, but first things first...
# TODO: Let's capitalize the first letter of each word in each list using .capitalize()

print()
print(meats)                # printing list to visualize
print(meats[0])             # printing first index, ham

for food in meats:
    print(food.upper())                   # Capitalizing all letters

meats_cap = []                            # empty list, edited items to be added into
print(type(meats_cap))                    # printing variable type to double check
for food in meats: 
    meats_cap.append(food.capitalize())                  # adding each capitalized 'food' item into new list
print()
print(meats_cap)                                         # printing new list
print()

print(cheeses)                            # printing list to visualize
print(cheeses[2])                         # printing first index, pepper jack
print()

for food in cheeses:
    print(food.upper())                   # Capitalizing all letters

cheeses_cap = []                          # empty list, edited items to be added into
print()
for food in cheeses:
    cheeses_cap.append(food.title())       # adding each capitalized 'food' item into new list

print()
print(cheeses_cap)                         # printing new list
print()




print('Question 2')
# Great! Your lists look much better. You need to come up with every combination of meats and cheeses for your menu.
# TODO: Use nested loops to create every combination of meat and cheese and add it to the sandwiches list

sandwiches = []

print()

for a in meats_cap:                              # Nested loop, combines both lists
    for b in cheeses_cap:
        sandwiches.append(a +" & " + b)

print(len(sandwiches))                           # print list length, or total combinations
print()

print(sandwiches)
print()

print('Question 3')
# TODO: Let's create an input to take a customer order for a sandwich, for example: 'Ham & Swiss'
# TODO: Loop over the sandwiches list.
# TODO: If it exists, print 'Great choice! 1 Ham & Swiss coming right up!'


order = input("What sandwich would you like? for example, 'Ham & Provolone': ")         # user input, specified format

print(f"You ordered a {order} sandwich")
print()



for sandwich in sandwiches:
    if order == sandwich:                                                              # if the order is on the sandwiches list, print
        print(f"Great choice, 1 {order} sandwich coming right up")

   


    


  

    
