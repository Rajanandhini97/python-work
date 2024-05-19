from city_functions import get_formatted_location


def test_city_country():
    """Validate city country display format"""
    formatted_location = get_formatted_location('santiago', 'chile')
    assert formatted_location == 'Santiago, Chile'


def test_city_country_population():
    """Validate city country display format"""
    formatted_location = get_formatted_location('santiago', 'chile', '50000')
    assert formatted_location == 'Santiago, Chile - population 50000'