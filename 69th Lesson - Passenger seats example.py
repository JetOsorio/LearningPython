def assign_seat(seat, *requests):
    print("\nAssign seat number " + str(seat) + ' the following passenger requests: ')
    for request in requests:
        print("- " + request)


assign_seat(36, "window seat", "breakfast")
