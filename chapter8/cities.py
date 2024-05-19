def describe_city(name, country='India'):
    """Describe's city"""
    print(f"{name.title()} is in {country.title()}")


describe_city('chennai')
describe_city('toronto', 'canada')
describe_city(name='kochi')