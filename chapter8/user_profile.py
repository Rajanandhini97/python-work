def build_profile(first, last, **user_info):
    """Print user info"""
    user_info['firstname'] = first
    user_info['lastname'] = last

    return user_info


# user_profile = build_profile('Nandhini', 'Nallusamy', location='Chennai', age=26)
# print(user_profile)