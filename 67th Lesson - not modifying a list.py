def passengers(notCheckedIn, checkedIn):
    # Simulate passengers who are not checked in
    while notCheckedIn:
        currentPassenger = notCheckedIn.pop()

        # Simulate checking in passenger
        print("Checking in passenger: " + currentPassenger)
        checkedIn.append(currentPassenger)


def showCheckedInPassengers(checkedIn):
    # Show all passengers who have checked in
    print("\nThe following passengers have been checked in: ")
    for passengers in checkedIn:
        print(passengers)


notCheckedIn = ["Rimjob Bob", "Kimothy Possible", 'Frank Spank']
checkedIn = []

passengers(notCheckedIn, checkedIn)
showCheckedInPassengers(checkedIn)

# current lesson starts here
passengers(notCheckedIn[:], checkedIn)  # makes copy of list
