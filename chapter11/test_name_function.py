from name_function import get_formatted_name


def test_first_last_name():
    """Do names like 'Nandhini Nallusamy' work?"""
    formatted_name = get_formatted_name('nandhini', 'nallusamy')
    assert formatted_name == 'Nandhini Nallusamy'


def test_first_last_middle_name():
    """Do names like 'Raja Nandhini Nallusamy' work?"""
    formatted_name = get_formatted_name('raja', 'nallusamy', 'nandhini')
    assert formatted_name == 'Raja Nandhini Nallusamy'
