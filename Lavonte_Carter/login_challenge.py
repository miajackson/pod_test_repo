# Feel free to update the values in the user dictionary
user = {
    'name': 'Laovnte Carter',
    'email': 'lavonte.carter@gmail.com',
    'password': 'abc123'
}

# Here is a while loop that runs as long as the email is incorrect
# When the correct email is entered, we exit the while loop and move to the next input for password
email = input('Email:')

# Checks the value of email in line 10
while(email != user['email']):
    # This code runs as long as the emails do not match
    print('This email does not exist in our system. Please try again.')
    # Ask to input email again and update value of email in line 10
    email = input('Please enter your email: ')

# Seeing 'Password: ' in command line means we have exited the while loop
password = input('Please enter your password: ')

# TODO: Write a while loop that checks whether the password is incorrect.
while(password != user['password']):
#and While(password <= 3):
    print('You have entered the incorrect password')
    password = input('Please enter the correct password: ')
print('You have enter too many errors and have been exited out of the program')

#how to exit out after three interations?
# count verible "and count is less than 5"


# TODO: Print 'Logging In...'

print('Loggind in...')

# TODO: Print 'Welcome back, ' and the name in the user dictionary

print(f''Welcome back,' + user['name']')