# nested_dict.py

# The code below has been edited to the lessons result
# I did not append inside the function.
# As I prefer the function to perfom just the one task and
# leave the variable outside the function, return the resut of the function
# Then append the returned value to the list

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


def add_new_country(country, number_of_visits, cities_visited):
    new_country = {}

    new_country['country'] = country
    new_country['visits'] = number_of_visits
    new_country['cities'] = cities_visited
    travel_log.append(new_country)



add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])



print(travel_log)