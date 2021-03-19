'''
GOOGLING CHALLENGE! 

Today, we'll ask you to write a bunch of small pieces of code.

Unlike previous ones, we have NOT showed you the exact code you'll need to answer 
the questions.

So, you'll want to search out answers on the web, make sure you understand them, then 
try them out until they work!

For each question, you should also COPY THE LINK TO THE RESOURCE WHERE YOU FOUND THE 
SOLUTION in so that you can use it in the future too
'''


# 1A. Sort the below list in alphabetical order
print('QUESTION 1\n')

print("\n my_friends list before sorting".upper())
my_friends = ['Yusuf', 'Aedan', 'Mia', 'Ash', 'Paul', 'Aeshna', 'Aryn', 'Rob']

# Printing the my_friends list before using ".sort()" function, establish base
print(my_friends)

# Sorting list with the ".sort()" function
my_friends.sort()

print("\n my_friends list sorted:".upper())

# Printing the list, which should be saved/updated in alphabetical order
print(my_friends)

# The resource used for sorting a list alphabetically
# https://stackoverflow.com/questions/14032521/python-data-structure-sort-list-alphabetically




print('\n\nQUESTION 2\n')

my_account = {'username': 'pbloom',
			  'password': 'python3.7',
			  'balance': 101.8,
			  'transaction_dates': ['9/18/2020', '9/20/2020', '10/5/2020'],
			  'verified': True}

# The ".keys()" function returns list of specified dictionary keys

print("\nUsing .key() function to print list\n".upper())
# In print command, add the ".keys()" function 
print(my_account.keys())

# Resource for using giving a list of dictionary keys
# https://stackoverflow.com/questions/5904969/how-to-print-a-dictionarys-key



print('\n\nQUESTION 3\n')
my_string = 'how much wood could a woodchuck chuck if a woodchuck could chuck wood?'

# The ".count()" function counts the amount of a specified argument within a string
# The arguments within the parenthesis will be counted

print(f"\"wood\" appears {my_string.count('wood')} times")


# resource for .count() function
# https://www.askpython.com/python/string/python-count-method





print('\n\nQUESTION 4\n')
my_list = ['apple', 'banana', 'banana', 'cherry', 'mango', 'banana', 'banana', 'banana']


# Similar to question 3, we are using the .count() function with my_list

print(f"Banana appears {my_list.count('banana')} times")

# resource for .count() function
# https://www.askpython.com/python/string/python-count-method



print('\n\nQUESTION 5\n')

# Using the "set()" function, converts the list to a set

unique_my_list = set(my_list)
print("The unique strings in my_list".upper())
print(unique_my_list)

# Resource for "set()" function
# https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python



print('\n\nQUESTION 6\n')

import numpy as np
# Importing numpy

# Using the "np.random.rand" function with a parameter of 1 will give a random number between 
# 0 and 1
random_number = np.random.rand(1)
print(random_number)

# Resource for generating random number "np.random.rand"
# https://www.w3resource.com/python-exercises/numpy/basic/numpy-basic-exercise-17.php



'''
Nice job! Hopefully after doing this challenge you feel a bit more ready to be able to 
search out new code solutions.

We'll be doing more challenges like this coming up in the future. 

Remember to comment all your code and push your work to your Github repo when you're done!
'''
