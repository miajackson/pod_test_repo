import random

person = [ "Colonel Mustard", 
            "Professor Plum", 
            "Mrs. White" ]

item = [ "a knife",
          "a hammer",
          "three ballpoint pens"]


random_person = random.choice(person)
random_item = random.choice(item)

print(f"The butler has been assassinated! Was it {random_person} with {random_item}?")

