meal = float(input("What is your meal amount: "))
tip = int(input("Enter tip %: "))
tax = .10
print("\n")
tip_amt = meal * tip/100
tax_amt = meal * tax
total = meal + tip_amt + tax_amt
print(f"\nThe total meal was ${meal:.2f} and your tip was ${tip:.2f}")
print(f"The total with tax is ${total:.2f}.\n")

number_of_people = (input("How many people are splitting the bill?: "))
print("\n")
