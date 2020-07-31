birthdayMonths = ['narch', 'may', 'june', 'august', 'december']
print(birthdayMonths)

birthdayMonths[0] = 'march'  # edits first item in list
print(birthdayMonths)

birthdayMonths.append('november')  # adds new item to list
print(birthdayMonths)

birthdayMonths = []  # empties list
print(birthdayMonths)

birthdayMonths.append('april')
print(birthdayMonths)

birthdayMonths.insert(0, 'january')  # adds item to specific spot on list
print(birthdayMonths)

del birthdayMonths[1]  # deletes item on specific index
print(birthdayMonths)
