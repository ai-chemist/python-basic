human_0 = {'name' : 'arthur', 'age' : 30,}
human_1 = {'name' : 'john', 'age' : 40,}
human_2 = {'name' : 'matt', 'age' : 20,}

humans = [human_0, human_1, human_2]

for human in humans:
    print(human)
    for key, value in human.items():
        print(f"{key} ::: {value}")
    print("\n")

animal_0 = {'name' : 'cat', 'owner' : 'mac',}
animal_1 = {'name' : 'dog', 'owner' : 'jack',}
animal_2 = {'name' : 'lion', 'owner' : 'drinkwater',}

pets = [animal_0, animal_1, animal_2]

for pet in pets:
    for key, value in pet.items():
        print(f"{key} ::: {value}")
    print("\n")

favorite_places = {
    'arthur' : ['new york'],
    'james' : ['new jersey', 'silent hill'],
    'morgan' : ['black water', 'new york', 'texas'],
}

for name, places in favorite_places.items():
    print(name.title())
    if len(places) <= 1:
        print(f"\tA favorite place : {places[0].title()}")
    else:
        for place in places:
            print(f"\tPlaces : {place.title()}")


favorite_numbers = {
    'a' : [1, 2, 3],
    'b' : [4, 5, 6],
    'c' : [7, 8, 9],
}

for name, nums in favorite_numbers.items():
    print(name.title())
    for num in nums:
        print(f"\t{num}")


cities = {
    'texas' : {'country' : 'united state of america', 'population' : 20000, 'fact' : 'stone cold'},
    'tokyo' : {'country' : 'japan', 'population' : 30000, 'fact' : 'not china'},
    'seoul' : {'country' : 'korea', 'population' : 40000, 'fact' : 'concrete hell'},
}

for city, city_info in cities.items():
    print(city.title())
    for key, value in city_info.items():
        print(f"{key.title()} : {value}")
    print("\n")