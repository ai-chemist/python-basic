rivers = {
    'egypt' : 'nile',
    'brazil' : 'amazon',
    'afghanistan' : 'amu darya',
    }

for country, river in rivers.items():
    print(f"The {river.title()} flows through {country.title()}")