'''
Planning & pseudocode challenge!

For each piece here, write out the pseudocode as comments FIRST, then write your code!

At many points, you'll have to choose between using a list vs. dictionary. Justify your choices!
'''


'''
1. Shipping

You are building a system to handle shipping orders. Each order should have 3 pieces of information:
-destination (string) (for the purposes of this challenge this can be any place, no need to make a full address)
-date_shipped (string)
-weight (float) (how many pounds the package is)

Will you choose to make each shipping order as a dictionary or list? Why?



Assign 3 separate orders to 3 separate variables
'''
#Make a dictionary for each order with 3 key value pairs for each piece of info.
print('\nPART 1')


order_1 = {'destination':'Brooklyn', 'date_shipped': '04/07/20', 'weight': 3.40}
order_2 = {'destination':'Queens', 'date_shipped': '11/23/20', 'weight': 1.20}
order_3 = {'destination':'Manhatten', 'date_shipped': '09/11/20', 'weight': 123.40}



'''
2. Building the database

Now, let's put the orders all into a database togther (all the orders are stored in 1 variable). 

Your database as a whole can either be a dictionary or a list (hint, you'll want nesting!). 

Print out the database to make sure all the info is in there. 

'''
print('\nPART 2')
#Make a variable for the database and a list for it. Put the three orders in the list.
database_list = [order_1, order_2, order_3]
#Print the database
print(database_list)


'''
3. Define a function called add_order() that adds one more order to your database, and make sure it works!
Any new orders should be in the same format as your existing ones. 
'''
print('\nPART 3')
#assign my 2 new variables for 2 more orders.
#make my function take 2 arguements for my orders which is a dictionary and my database which is a list. 
# I'll append both orders to the dictionary.

order_4 = {'destination':'Bronx', 'date_shipped': '04/19/21', 'weight': 12.31}

def add_order(database, order):
    database_list.append(order)

add_order(database_list,order_4)

print(database_list)



'''
4. Define a function called complete_order() to mark a specific order in your database complete

This means you'll need a new piece of data inside the order that is True when the order is complete.

Test this out and print out your database to make sure it works!

HINT: Think about how your choice of list/dictionary in part 2 informs how someone would reference an order in the database
'''
print('\nPART 4')
#make a function for order completion
#since its a list it would be an index used for reference.
#checking for the first item in the list which is index zero bc its a list.
# in the the function parameter for the dictionary create a key called 'completed' and set it to True
def complete_order(database, order_index):
	database[0]['completed'] = True


complete_order(database_list, 0)
print(database_list)

    	
	


