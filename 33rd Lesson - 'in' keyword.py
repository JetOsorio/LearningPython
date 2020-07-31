registeredNames = ['bob', 'chad', 'kyle', 'karen', 'neel']

username = input("Please enter the username you would like to use. ")

# Checks if username is in list
if username in registeredNames:
    print("Sorry, username is already taken.")
else:
    print("Username is available")
    registeredNames.append(registeredNames)
