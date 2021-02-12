print("Challenge: Favourite Restaurants")

print()

print("Question 1")

print("Below is a dictionary consisting of details of 1 restaurant fetched from Yelp. Go through the dictionary and print out the following 3 pieces of information about the restaurant: \n1. The latitude and longitude of Four Barrel Coffee \n2. The complete address of Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code. \n3. The website of Four Barrel Coffee.")

restaurant = {
    "name": "Four Barrel Coffee",
    "url": "https://www.yelp.com/biz/four-barrel-coffee-san-francisco",
    "latitude": 37.7670169511878,
    "longitude": -122.42184275,
    "city": "San Francisco",
    "country": "US",
    "address2": "",
    "address3": "",
    "state": "CA",
    "address1": "375 Valencia St",
    "zip_code": "94103",
    "distance": 1604.23,
    "transactions": ["pickup", "delivery"]
}

print(restaurant)
print(f'Latitude : {restaurant["latitude"]} Longitude : {restaurant["longitude"]}')
print(f'The complete address of the place is {restaurant["address1"]}, {restaurant["city"]}, {restaurant["state"]} {restaurant["country"]} {restaurant["zip_code"]}')
print(f'The website of the place is: {restaurant["url"]}')




print("Question 2")

fav_restaurants = {"Peter Lugers": ["178 Broadway, Brooklyn, NY 11211", "steak well done", "8 AM - 10 PM"], 
"John Goes": ["178 Fleet st, NY, NY 10002", "baked ziti", "8 AM - 10 PM"], 
"Bellas": ["123 Broad st, Brooklyn, NY 11234", "Burger", "7 AM - 9 PM"]}
print(fav_restaurants)


print("Question 3")

print("Imagine that any 1 of your most favourite restaurants closed down during the Covid. Remove the details of that restaurant from the dictionary fav_restaurants.")

fav_restaurants.pop("Peter Lugers")

print(fav_restaurants)

print("Question 4")

print("Imagine that another one of your most favourite restaurants modified its opening and closing hours during Covid. Update just the hours field (3rd value of the list) for 1 restaurant in the dictionary fav_restaurants.")

regular_hours = fav_restaurants["Bellas"][2]
fav_restaurants["Bellas"][2] = "7-5PM"
corona_hours = fav_restaurants["Bellas"][2]
print(fav_restaurants)

print(f'The old hours of Bellas were {regular_hours} and the post corona hours are {corona_hours}.')