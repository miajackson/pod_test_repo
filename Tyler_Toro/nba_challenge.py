#CHALLENGE 2.1
print("Challenge 2.1:")
jamal_murray_3pts_made = 46
fred_vanvleet_3pts_made = 43
james_harden_3pts_made = 37

#CHALLENGE 2.2
print("Challenge 2.2:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots")
print(f"In the 2020 NBA playoffs, Fred VanVleet made {fred_vanvleet_3pts_made} 3 point shots")
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3 point shots")
print()

#CHALLENGE 2.3
print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
jamal_murray_attempts = 93
fred_vanvleet_attempts = 110
james_harden_attempts = 109
print()

#CHALLENGE 2.4
print("Challenge 2.4: Build on your print statement")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots and {jamal_murray_attempts} 3 point shot attempts")
print(f"In the 2020 NBA playoffs, Fred VanVleet made {fred_vanvleet_3pts_made} 3 point shots and {fred_vanvleet_attempts} 3 point shot attempts")
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3 point shots and {james_harden_attempts} 3 point shot attempts")
print()

#CHALLENGE 2.5
print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
# ALSO LIKE THIS::: jamal_perc = 46/93
jamal_perc = jamal_murray_3pts_made/jamal_murray_attempts
fred_perc = fred_vanvleet_3pts_made/fred_vanvleet_attempts
james_perc = james_harden_3pts_made/james_harden_attempts

print(f"In the 2020 NBA playoffs, Jamal Murray's shooting percentage was {jamal_perc}")
print(f"In the 2020 NBA playoffs, Fred VanVleet's shooting percentage was {fred_perc}")
print(f"In the 2020 NBA playoffs, James Harden's shooting percentage was {james_perc}")

print()
#CHALLENGE 3.1
print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
print()
print("The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis. \
\nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. \
\nThose three have made good developments with the Pelicans, especially Brandon Ingram. \
\nBut, the deal is still a huge win for the Lakersas Lebron, Davis, and company have put together an incredible season. \
\nLos Angeles has riddenJames and Davis, along with a supporting cast built around them, to the second-best record in the NBA. \
\nThe Lakers ended the season atop the Western Conference with a record of 49-14. \
\nThey were narrowly behind the Bucks for the best record in the league. \
\nDavis proved to the final piece necessary forthe Lakers to rebound from missing the playoffís last year. \
\nLos Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.")
print()

#CHALLENGE 3.2
print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
phrase = "The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis. \
\nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. \
\nThose three have made good developments with the Pelicans, especially Brandon Ingram. \
\nBut, the deal is still a huge win for the Lakersas Lebron, Davis, and company have put together an incredible season. \
\nLos Angeles has riddenJames and Davis, along with a supporting cast built around them, to the second-best record in the NBA. \
\nThe Lakers ended the season atop the Western Conference with a record of 49-14. \
\nThey were narrowly behind the Bucks for the best record in the league. \
\nDavis proved to the final piece necessary forthe Lakers to rebound from missing the playoffís last year. \
\nLos Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season."

print(phrase.upper())
#CHALLENGE 3.3
print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
# TODO: make a variable called `lakers_are_best` to indicate this
# TODO: print out the variable in an f-string to convey your opinion on the lakers
lakers_are_best = True
print(f"It's {lakers_are_best}, I think the Lakers are the greatest of all time")
print()
#CHALLENGE 3.4
print('Challenge 3.4: Type Conversion')
print(int(lakers_are_best))
print(float(lakers_are_best))
print()
#CHALLENGE 3.5
print('Challenge 3.5: Type Conversion Part 2')
print()
print(str(jamal_perc))
print(str(fred_perc))
print(str(james_perc))
print()
print(int(jamal_perc))
print(int(fred_perc))
print(int(james_perc))
print()

#What if we multiply by 100?
print()
print(str(jamal_perc*100))
print(str(fred_perc*100))
print(str(james_perc*100))
print()
print(int(jamal_perc*100))
print(int(fred_perc*100))
print(int(james_perc*100))

##Done


