def get_formatted_location(city, country, population=''):
    """Neatly formatted location"""
    if population:
        formatted_location = f"{city.title()}, {country.title()} - population {population}"
    else:
        formatted_location = f"{city.title()}, {country.title()}"
    return formatted_location
