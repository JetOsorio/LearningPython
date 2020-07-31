rentalProperties = {}

rentalOpen = True
while rentalOpen:
    username = input("\nWhat is your name? ")
    rentalProperty = input("What is the address of the property you want to rent? ")

    rentalProperties[username] = rentalProperty

    repeat = input("\nDo you know anyone who might like to rent out their property? ")
    if repeat.lower() == 'no':
        rentalOpen = False

print("\n=== Property to rent ===")
for username, rentalProperty in rentalProperties.items():
    print(username.title() + " has " + rentalProperty.title() + " to rent.")