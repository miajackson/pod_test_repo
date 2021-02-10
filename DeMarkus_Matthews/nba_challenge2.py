print("Challenge 2.1:")
jamal_murray_3pts = 46
james_harden_3pts = 37
fred_vanvleet_3pts = 43
# <-------------------->

print("Challenge 2.2:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts} 3 point shots")
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts} 3 point shots")
print(f"In the 2020 NBA playoffs, Fred VanVleet made {fred_vanvleet_3pts} 3 point shots")
# <-------------------->

print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
jamal_murray_attempt = 93
james_harden_attempt = 109
fred_vanvleet_attempt = 110

print("Challenge 2.4: Build on your print statement")
print(f"In the 2020 NBA playoffs, Jamal Murray attempted {jamal_murray_attempt} 3 point shots but only made {jamal_murray_3pts} 3 point shots")
print(f"In the 2020 NBA playoffs, Fred VanVleet attempted {fred_vanvleet_attempt} 3 point shots but only made {fred_vanvleet_3pts} 3 point shots")
print(f"In the 2020 NBA playoffs, Fred VanVleet attempted {james_harden_attempt} 3 point shots but only made {james_harden_3pts} 3 point shots")
# <-------------------->

print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
jamal_murray_percentage = int(100 * (jamal_murray_attempt / jamal_murray_3pts))
james_harden_percentage = int(100 * (james_harden_attempt / james_harden_3pts))
fred_vanvleet_percentage = int(100 * (fred_vanvleet_attempt / fred_vanvleet_3pts))

fred_vanvleet_percentage = str(fred_vanvleet_percentage)[0:2]
james_harden_percentage = str(james_harden_percentage)[0:2]
jamal_murray_percentage = str(jamal_murray_percentage)[0:2]
print(type(jamal_murray_percentage))
print(f"In the 2020 NBA playoffs, Fred VanVleet has a {fred_vanvleet_percentage}% shooting percentage")
print(f"In the 2020 NBA playoffs, Jamal Murray has a {jamal_murray_percentage}% shooting percentage")
print(f"In the 2020 NBA playoffs, James Harden has a {james_harden_percentage}% shooting percentage")
# <-------------------->

print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
laker_statement = 'The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis. They sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. Those three have made good developments with the Pelicans, especially Brandon Ingram. But, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season. Los Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA. The Lakers ended the season atop the Western Conference with a record of 49-14. They were narrowly behind the Bucks for the best record in the league. Davis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year. Los Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.'

def print_new_line(statement):
    result = ''
    for char in statement:
        if(char != '.'):
            result += char
        else:
            result += f'{char}\n'
    return result

print(print_new_line(laker_statement))
# <-------------------->

print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
print(print_new_line(laker_statement).upper())
# <-------------------->

print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
lakers_are_best = True
print(f"It is {lakers_are_best} that the Lakers are the best basketball team")
# <-------------------->

print('Challenge 3.4: Type Conversion')
lakers_are_best = int(lakers_are_best)
print(lakers_are_best)
lakers_are_best = float(lakers_are_best)
print(lakers_are_best)
# <-------------------->

print('Challenge 3.5: Type Conversion Part 2')
jamal_murray_percentage = str(jamal_murray_percentage)
james_harden_percentage = str(james_harden_percentage)
fred_vanvleet_percentage = str(fred_vanvleet_percentage)
print(jamal_murray_percentage)
print(james_harden_percentage)
print(fred_vanvleet_percentage)

jamal_murray_percentage = int(jamal_murray_percentage)
james_harden_percentage = int(james_harden_percentage)
fred_vanvleet_percentage = int(fred_vanvleet_percentage)
print(jamal_murray_percentage)
print(james_harden_percentage)
print(fred_vanvleet_percentage)
