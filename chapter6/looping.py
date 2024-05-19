# # 6-5
#
# rivers = {
#     'nile': 'egypt',
#     'kaveri': 'india',
#     'mississippi': 'united states'
# }
#
# for k, v in rivers.items():
#     print(f"The {k.title()} runs through {v.title()}.")
# print("\n")
#
# for key in rivers:
#     print(f"River {key}")
# print("\n")
#
# for values in rivers.values():
#     print(f"Country {values}")
# print("\n")

# 6-6 polling
fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

friends = ['phil', 'sarah', 'emily', 'hailey', 'alex']

for friend in friends:
    if friend in fav_languages.keys():
        print(f"{friend.title()}, thank you for your response")
    else:
        print(f"{friend.title()} please take our poll!")

