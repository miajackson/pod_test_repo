# Algorithmic Challenge


print("Question 1")
print()

fruit_list = ["apple", "orange", "banana", "pear", "grape", "pineapple"]
fruit = "pear"
# Write the time complexity for the function below, check_if_fruit_in_list

def check_if_fruit_in_list(my_list, fruit):
    for fruit_item in my_list:
        if fruit_item == fruit:
            print("Fruit in list!")
    print("Fruit not in list!")


# TODO Write the time complexity

'''
We have a list, and a for loop

The function check_if_fruit_in_list is O(n), linear time, the amount of potential operations 
increases with the size of the list, fruit_list

'''

# For Questions 2 and 3, we are going to look at the time complexities for the previous deli meats challenge

meats = ['ham', 'turkey', 'chicken', 'tuna']
cheeses = ['cheddar', 'swiss', 'pepper jack', 'provolone']

print("Question 2")
print()
# Write the time complexity for the function below, capitalize_meats_and_cheeses
def capitalize_meats_and_cheeses(meats, cheeses):
    for i in range(len(meats)):
        meats[i] = meats[i].capitalize()

    for i in range(len(cheeses)):
        cheeses[i] = cheeses[i].capitalize()

# TODO Write the time complexity

'''
O(n)***

The function, capitalize_meats_and_cheeses, has a linear time complexity  ( O(n)). Each for-loop
within the function is ran by the number of each item in the list. This is a linear relationship.

'''

print("Question 3")
print()
# Write the time complexity for the function below, deli_meat_challenge
def deli_meat_challenge(meat, cheeses, sandwiches):
    for meat in meats:
        for cheese in cheeses:
            sandwiches.append(f'{meat} & {cheese}')
    return sandwiches

# TODO Write the time complexity

'''
O(n^2)***

Each inner loop multiplies itself by the outer loop in nested loop arrangement. The function, 
deli_meat_challenge, has an exponential time complexity because there are two for-loops.
'''


print("Question 4")
print()

'''
For the following question, you will be given an unsorted array that may contain duplicates. 
Your job is to write a function that returns true if there are duplicates and false if not.
Then write the time complexity of that function and think of if there are anyways you could have
made the algorithm more efficient? 
''' 

my_list = [5,2,3,4,5,8]
def contains_duplicates(my_list):
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            if my_list[i] == my_list[j]:
                return True
    return False



# TODO Write the time complexity
'''
O(n^2)

The function contains_duplicates has a quadratic time complexity because there are nested loops. 

'''
## Bonus!
# Write a function that solves the problem, contains_duplicates in less time (i.e. lower time complexity).
