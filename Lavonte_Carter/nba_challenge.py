print("Challenge 2.1:")
jamal_murray_3pts_made = 46
fred_vanvleet_3pts_made = 43
james_harden_3pts_made = 37

# TODO: Create variable here for number of 3 pt shots made by Fred VanVleet
# TODO: Create variable here for number of 3 pt shots made by James Harden

print("Challenge 2.2:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots")
print(f"In the 2020 NBA playoffs, Fred Vlanvleet made {fred_vanvleet_3pts_made} 3 point shots")
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3 point shots")

# TODO: Create print statement here for Fred VanVleet
# TODO: Create print statement here for James Harden
print()

print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
jamal_murray_3pts_attempted = 93
fred_vanvleet_3pts_attempted = 110
james_harden_3pts_attempted = 109

#print Challenge 2.3
print(f"In the 2020 NBA playoffs, Jamal Murray attempted {jamal_murray_3pts_attempted} 3 point shots")
print(f"In the 2020 NBA playoffs, Fred Vlanvleet attempted {fred_vanvleet_3pts_attempted} 3 point shots")
print(f"In the 2020 NBA playoffs, James Harden attempted {james_harden_3pts_attempted} 3 point shots")

# TODO: Create variable here for number of 3 pt shot attempts by Jamal Murray
# TODO: Create variable here for number of 3 pt shot attempts by Fred VanVleet
# TODO: Create variable here for number of 3 pt shot attempts by James Harden
print()

print("Challenge 2.4: Build on your print statement")

#print("Challenge 2.4:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots, and attempted {jamal_murray_3pts_attempted} shots")
print(f"In the 2020 NBA playoffs, Jamal Murray made {fred_vanvleet_3pts_made} 3 point shots, and attempted {fred_vanvleet_3pts_attempted} shots")
print(f"In the 2020 NBA playoffs, Jamal Murray made {james_harden_3pts_made} 3 point shots, and attempted {james_harden_3pts_attempted} shots")
# TODO: Copy the three print statements you wrote in Challenge 2.2 and extend them to also print
# the number of three point shots for each player. E.g., output should be similar to
# "In the 2020 NBA playoffs, player X made Y 3 point shots and Z 3 point shot attempts."
print()

print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
jamal_murray_3pts_percentage = jamal_murray_3pts_made/jamal_murray_3pts_attempted
fred_vanvleet_3pts_percentage = fred_vanvleet_3pts_made/fred_vanvleet_3pts_attempted
james_harden_3pts_percentage = james_harden_3pts_made/james_harden_3pts_attempted

#creating print statement for player 3 point percentages
print(f"In the 2020 NBA playoffs, Jamal Murray 3 point percentages were {jamal_murray_3pts_percentage}")
print(f"In the 2020 NBA playoffs, Fred Vanvleet 3 point percentages were {fred_vanvleet_3pts_percentage}")
print(f"In the 2020 NBA playoffs, Jamal Murray 3 point percentages were {james_harden_3pts_percentage}")

# TODO: Calculate the three point percentage, which is given by `three points made/three point attempts`
# TODO: Calculate and print the 3 point percentage for Jamal Murray
# TODO: Calculate and print the 3 point percentage for Fred VanVleet
# TODO: Calculate and print the 3 point percentage for James Harden
print()


print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')

# TODO: Print the giant chunk of text out using escape characters so each sentence comes out on a new line
#Below is a big paragraph of text about the Lakers 2020 season from https://www.lineups.com/nba/roster/los-angeles-lakers

'''
The Lakers went all in this offseason 
and swung a deal for former Pelicans forward Anthony Davis. 
They sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, 
and 3 first-round picks to New Orleans to land Davis. 
Those three have made good developments with the Pelicans, especially Brandon Ingram. 
But, the deal is still a huge win for the Lakers as Lebron, Davis, 
and company have put together an incredible season. 
Los Angeles has ridden James and Davis, 
along with a supporting cast built around them, 
to the second-best record in the NBA. 
The Lakers ended the season atop the Western Conference with a record of 49-14. 
They were narrowly behind the Bucks for the best record in the league. 
Davis proved to the final piece necessary for the Lakers to 
rebound from missing the playoffís last year. 
Los Angeles was a dominant club on both sides of the ball 
and are in a position to have another successful year next season.
'''

print(f"The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis. \nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. \nThose three have made good developments with the Pelicans, especially Brandon Ingram. \nBut, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season. \nLos Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA. \nThe Lakers ended the season atop the Western Conference with a record of 49-14. \nThey were narrowly behind the Bucks for the best record in the league. \nDavis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year. \nLos Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.")

print()

print('Challenge 3.2 Print out the paragraph with only 1 sentence per line, and all in upper case.')
# TODO: Print out the paragraph with only 1 sentence per line
# TODO: Print out the paragraph with all upper case.

str_1 = 'The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis. \nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. \nThose three have made good developments with the Pelicans, especially Brandon Ingram. \nBut, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season. \nLos Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA. \nThe Lakers ended the season atop the Western Conference with a record of 49-14. \nThey were narrowly behind the Bucks for the best record in the league. \nDavis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year. \nLos Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.'
print(str_1.upper())

print()

print('Challenge 3.3 Are the Lakers the best team?')
# TODO: Make a boolean variable called lakers_are_best
# TODO: Indicate, whether the following statement is true: The Lakers are the best basketball team in the NBA
# TODO: Using an f-string containing your lakers_are_best variable 
# TODO: Print out your evaluation of whether the statement was true or not

lakers_are_best = False
output = lakers_are_best

print(f"The statement that the Lakers are currently best basketball team in the NBA is {output}")

print()

print('Challenge 3.4: Type Conversion')
# TODO: Convert your `lakers_are_best` variable to an integer, and print it out. 
#TODO: Ansswr question as to why do you think it takes this value?
#It has not been assigned a numeric value yet

lakers_are_best = int(lakers_are_best)
print(lakers_are_best)

# TODO: Convert your `lakers_are best` variable to a float, and print it out

lakers_are_best = float(lakers_are_best)
print(lakers_are_best)

print()

print('Challenge 3.5: Type Conversion Part 2')
print()
# TODO: Take each player's three point percentage (from part 2.5) and convert it to a string, then print it out.

jamal_murray_3pts_percentage = str(jamal_murray_3pts_percentage)
print(jamal_murray_3pts_percentage)
fred_vanvleet_3pts_percentage = str(fred_vanvleet_3pts_percentage)
print(fred_vanvleet_3pts_percentage)
james_harden_3pts_percentage = str(james_harden_3pts_percentage)
print(james_harden_3pts_percentage)

print()

# TODO: Take each player's three point percentage (from part 2.5) and convert it to an integer, then print it out.

