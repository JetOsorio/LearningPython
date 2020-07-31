def formattedName(firstName, lastName):
    fullName = firstName + ' ' + lastName
    return fullName.title()

person = formattedName('rimjob', 'bob')
print(person)

def getFormattedUsername(emailAddress):
    username = emailAddress.strip() #remember 'strip' removes blank space before and after string
    return username
user = getFormattedUsername('   osoriojet@gmail.com    ')
print(user)