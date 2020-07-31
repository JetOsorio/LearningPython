def create_passenger(*requests):  # The '*' tells python to make an empty tuple called requests, and put in any value
    # it receives
    print(requests)


create_passenger('window seat', 'seat near top of plane', 'pre-order breakfast')

#Arbituary arguments with for loop
def create_passenger(*requests):
    print("\nThis passenger has requested: ")
    for request in requests:
        print("- " + request)

create_passenger('window seat', 'top of plane', 'breakfast')
