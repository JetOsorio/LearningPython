birthdayMonths = {
    'bob': 'march',
    'john': 'december',
    'karen': 'august',
    'noah': 'may',
    'mina': 'august'
}

for name in birthdayMonths.keys():  # displays only the keys in the dictionary
    print(name.title())

for months in birthdayMonths.values():  # displays only the values in the dictionary
    print(months.title())

print("\n")

for months in set(birthdayMonths.values()):  # 'set' does not allow for repeating values
    print(months.title())
