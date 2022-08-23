'''
GOOGLING CHALLENGE! 
Today, we'll ask you to write a bunch of small pieces of code.
Unlike previous ones, we have NOT showed you the exact code you'll need to answer the questions.
So, you'll want to search out answers on the web, make sure you understand them, then try them out until they work!
For each question, you should also COPY THE LINK TO THE RESOURCE WHERE YOU FOUND THE SOLUTION in so that you can use it in the future too
'''
# *** Website link information towards the end of this challenge***

# 1A. Sort the below list in alphabetical order
print('QUESTION 1\n')
my_friends = ['Yusuf', 'Aedan', 'Mia', 'Ash', 'Paul', 'Aeshna', 'Aryn', 'Rob']


my_friends.sort()
print(my_friends)

print("my_friends list sorted: .upper()")

# 1B. Comment your code in 1A to convince yourself you understand how it works
# ***Used the python data structure to sort 'my_friends' list alphabetically on stackoverflow*** 

# 2A. Get all the keys from the below dictionary, then print them out:
# Hint: there is a single command that can do this
print('QUESTION 2\n')

my_account = {'username': 'pbloom',
			  'password': 'python3.7',
			  'balance': 101.8,
			  'transaction_dates': ['9/18/2020', '9/20/2020', '10/5/2020'],
			  'verified': True}

print(my_account.keys())

# 2B. Comment your code in 2A to convince yourself you understand how it works
# ***Used 'How to print a dictionary's key?' in stackoverflowto print the keys only***


# 3A Count how many times the word 'wood' appears in the following string:
# Hint: there is a single command that can do this
print('QUESTION 3\n')
my_string = 'how much wood could a woodchuck chuck if a woodchuck could chuck wood?'

print(my_string.count('wood'))

# 3B. Comment your code in 3A to convince yourself you understand how it works
# ***Used 'How to Use the Python count() Function' to count wood in 'my_string***


# 4A Count how many times the string 'banana' appears in the following list:
# Hint: there is a way to do this with one line of code
print('QUESTION 4\n')
my_list = ['apple', 'banana', 'banana', 'cherry', 'mango', 'banana', 'banana', 'banana']

print(my_list.count('banana'))

# 4B. Comment your code in 4A to convince yourself you understand how it works
# ***Used 'How can I count occurrences of a list item?' to findhow many times banana appears.***


# 5A Print out all of the unique strings in my_list
# Hint: there is a way to do this with one line of code
print('QUESTION 5\n')

mylist = list(set(mylist))

unique_list_items = set(my_list)
print(unique_list_items)

# 5B. Comment your code in 5A to convince yourself you understand how it works
# ***Used 'Python/Get unique values froma list' to print all of the unique strings.***

# 6A. Import numpy, then use it to generate a random number between 0-1
print('QUESTION 6\n')

import numpy as np

# 6B. Comment your code in 6A to convince yourself you understand how it works
# ***Used 'NumPy: Generate a random number between 0 and 1 to generate a random number between 0-1.***
random_number = np.random.rand(1)
print(random_number)

'''
Nice job! Hopefully after doing this challenge you feel a bit more ready to be able to search out new code solutions.
We'll be doing more challenges like this coming up in the future. 
Remember to comment all your code and push your work to your Github repo when you're done!
'''

# https://stackoverflow.com/questions/14032521/python-data-structure-sort-list-alphabetically
# Question 1
# https://stackoverflow.com/questions/5904969/how-to-print-a-dictionarys-key
# Question 2
# https://www.askpython.com/python/string/python-count-method
# Question 3
# https://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item
# Question 4
# https://www.geeksforgeeks.org/python-get-unique-values-list/
# Question 5
# https://www.w3resource.com/python-exercises/numpy/basic/numpy-basic-exercise-17.php
# Question 6
# https://chrisalbon.com/python/basics/generating_random_numbers_with_numpy/
# Question 