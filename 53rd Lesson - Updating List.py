unconfirmedUsers = ['tony', 'bob', 'karen', 'steve']

confirmedUsers = []

while unconfirmedUsers:
    currentUser = unconfirmedUsers.pop()  # Remember 'pop' deletes item from list to be moved to another
    print("Verifying user: " + currentUser.title())
    confirmedUsers.append(currentUser)

print("\nThe following users have been confirmed: ")
for confirmedUser in confirmedUsers:
    print(confirmedUser.title())
