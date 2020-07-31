adminUsers = ['bob', 'karen']

username = input("Please enter username. ")

#'not in' keyword checks if input is not in list of admin users
if username not in adminUsers:
    print("You do not have access!")
else:
    print("Access granted.")