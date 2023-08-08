# City Names

def city_country(city: str, country: str) -> str:

    formatted_name: str = f"\"{city.title()}, {country.title()}\""
    return formatted_name

name_city = city_country("London", "England")

print(name_city)
