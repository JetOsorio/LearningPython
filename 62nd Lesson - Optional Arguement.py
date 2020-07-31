def formattedName(firstName, lastName, middleName=''): #to make it optional, make its default value blank
    if middleName:
        fullName = firstName + ' ' + middleName + ' ' + lastName
    else:
        fullName = firstName + ' ' + lastName
    return fullName.title()


person = formattedName('bob', 'ross')
print(person)

person = formattedName('bob', 'ross', 'god-damn')
print(person)