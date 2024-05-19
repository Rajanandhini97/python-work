def city_country(name, country):
    """Returns formatted city name and country"""
    formatted_name = f"{name}, {country}"
    return formatted_name.title()

city = city_country('chennai', 'india')
print(city)

city = city_country('montreal', 'canada')
print(city)