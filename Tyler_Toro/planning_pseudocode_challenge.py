'''
Planning & pseudocode challenge!

For each piece here, write out the pseudocode as comments FIRST, then write your code!

At many points, you'll have to choose between using a list vs. dictionary. Justify your choices!



1. Shipping

You are building a system to handle shipping orders. Each order should have 3 pieces of information:
-destination (string) (for the purposes of this challenge this can be any place, no need to make a full address)
-date_shipped (string)
-weight (float) (how many pounds the package is)

Will you choose to make each shipping order as a dictionary or list? Why?

Assign 3 separate orders to 3 separate variables
'''
print('\nPART 1')

# Each order will be a dictionary, assigned to a variable. The keys will be destination, date_shipped, weight. By 
# storing the orders as dictionaries, we can have labeled data for later use

order_1 = {"destination": "500 Pearl st.", "date_shipped": "1/20/2021", "weight": 3.14}
order_2 = {"destination": "2121 Matthews ave", "date_shipped": "2/20/2021", "weight": 800.21}
order_3 = {"destination": "2855 Clafflin ave", "date_shipped": "3/3/2021", "weight": 15.78}


print()
print("\n First Order:".upper())
print(order_1)
print("\n First order type:".upper())
print(type(order_1))

'''
2. Building the database

Now, let's put the orders all into a database togther (all the orders are stored in 1 variable). 

Your database as a whole can either be a dictionary or a list (hint, you'll want nesting!). 

Print out the database to make sure all the info is in there. 

'''

# database variable will combine all three orders

database = [order_1, order_2, order_3]
print("\n Database type:".upper())
print(type(database))
print("\n database:\n".upper())
print(database)
print()
print('\nPART 2')


'''
3. Define a function called add_order() that adds one more order to your database, and make sure it works!
Any new orders should be in the same format as your existing ones. 
'''
#/////////
# we need to: create a function that adds to existing list
# the format needs to be in a dictionary
# new values will be matched to keys, added to blank dictionary, then the whole dictionary added to database
# A function that takes user input, saves input into correct dictionary format


print('\nPART 3')
print("\n PREVIOUS DATABASE:\n")
print(database)
print("\n")
# taking user input
def additional_order():
    #pass
    new_order = {}
    new_order["destination"] = input("Where is your package going:\n")
    new_order["date_shipped"] = input("When is this package shipping? \"M/DD/YYYY\"\n")
    new_order["weight"] = input("how much does your package weigh: \n")
    database.append(new_order)
    return

additional_order()
print("\n\n")
#checking the added order
print("Added order:\n")
print(database[3])

#prints updated list
print("\n\nUPDATED DATABASE:\n")
print(database)



print()




'''
4. Define a function called complete_order() to mark a specific order in your database complete

This means you'll need a new piece of data inside the order that is True when the order is complete.

Test this out and print out your database to make sure it works!

HINT: Think about how your choice of list/dictionary in part 2 informs how someone would reference an order in the database
'''
print('\nPART 4')


# I need to add a new  key/value pair to particular order
# In the list, database, orders are organized by index
# the new piece of the dictionary will have complete will be set to TRUE or FALSE
# The key "Order complete" will be added to order, and "TRUE" saved as value
# to call an order, an if statement could check for a valid key/value combo 

print("\nChecking date of first order:\n")
print(database[0]["date_shipped"])
print()

def complete_order():
    pass
    guest_check = input("Please enter order ship date: M/DD/YYYY\n")
    for i in range(len(database)):
        if guest_check == database[i]["date_shipped"]:
            database[i]["Complete"] = True
        else:
            pass
     


complete_order()

print("\n Updated database, with added info of order, order complete")
print(database)
