def describe_city(city, country = "USA"):
    print(f"{city.title()} in {country.upper()}")

describe_city("New York")
describe_city("Texas", "USA")
describe_city("Tokyo", "Japan")
describe_city(city = "Seoul", country = "Korea")