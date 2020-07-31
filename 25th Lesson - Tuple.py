# Tuples are lists that cannot change
dates = (1, 4, 6, 11)
print(dates[0])
print(dates[2])

coordinates = (1001, 5002)
print("\nOriginal Coordinates: ")
for coordinate in coordinates:
    print(coordinate)

coordinates = (2002, 7003)  # Only way to modify tuples is to create a new one
print("\nNew Coordinates")
for coordinate in coordinates:
    print(coordinate)
