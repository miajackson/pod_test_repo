print("Challenge 2.1:")
jamal_murray_3pts_made = 46
fred_vanvleet_3pts_made = 43
james_harden_3pts_made = 37

print("Challenge 2.2:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots")
print(f"In the 2020 NBA playoffs, Fred VanVleet made {fred_vanvleet_3pts_made} 3 point shots")
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3 point shots")

print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
jm_shot_attempts = 93
fv_shot_attempts = 110
jh_shot_attempts = 109
print()

print("Challenge 2.4: Build on your print statement")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots and made {jm_shot_attempts} shot attempts ")
print(f"In the 2020 NBA playoffs, Jamal Murray made {fred_vanvleet_3pts_made} 3 point shots and made {fv_shot_attempts} shot attempts ")
print(f"In the 2020 NBA playoffs, Jamal Murray made {james_harden_3pts_made} 3 point shots and made {jh_shot_attempts} shot attempts ")
print()

print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
# TODO: Calculate the three point percentage, which is given by `three points made/three point attempts`
# TODO: Calculate and print the 3 point percentage for Fred VanVleet
# TODO: Calculate and print the 3 point percentage for James Harden
jamal_sp = jamal_murray_3pts_made/jm_shot_attempts
fred_sp = fred_vanvleet_3pts_made/fv_shot_attempts
james_sp = james_harden_3pts_made/jh_shot_attempts


print(f"In the 2020 NBA playoffs Jamal Murray had a shooting percentage was {jamal_sp}")
print(f"In the 2020 NBA playoffs Jamal Murray had a shooting percentage was {fred_sp}")
print(f"In the 2020 NBA playoffs Jamal Murray had a shooting percentage was {james_sp}")

print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
# TODO: As above, orint out the paragraph with only 1 sentence per line, and all in upper case

print("The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis.\nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis.\nThose three have made good developments with the Pelicans, especially Brandon Ingram. \nBut, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season. \nLos Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA. \nThe Lakers ended the season atop the Western Conference with a record of 49-14. \nThey were narrowly behind the Bucks for the best record in the league. \nDavis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year. \nLos Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.".upper())
print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
# TODO: make a variable called `lakers_are_best` to indicate this
# TODO: print out the variable in an f-string to convey your opinion on the lakers

lakers_are_best = False
print(lakers_are_best)
print('Challenge 3.4: Type Conversion')
# TODO: Convert your `lakers_are_best` variable to an integer, and print it out. 
# TODO: Convert your `lakers_are best` variable to a float, and print it out
print(int(lakers_are_best))
print(float(lakers_are_best))
print('Challenge 3.5: Type Conversion Part 2')
# TODO: Take each player's three point percentage (from part 2.5) and convert it to a string, then print it out.
# TODO: Take each player's three point percentage (from part 2.5) and convert it to an integer, then print it out.
#3.5
#converting into string
print(str(jamal_sp))
print(str(fred_sp))
print(str(james_sp))
#converting into interger
print(int(jamal_sp))
print(int(fred_sp))
print(int(james_sp))