def city_country(city, country, population=None):
    """City Country"""
    if population:
        return f"{city.title()}, {country.title()} : {population}"
    else:
        return f"{city.title()}, {country.title()}"