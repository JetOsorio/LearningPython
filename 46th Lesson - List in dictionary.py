orderedCar = {
    'type' : 'standard four saloon',
    'extras' : ['alloy wheels', 'climate control', 'leather heated seats'] #List can be used as a value in dictionary
}

print("The car you ordered is a " + orderedCar['type'] + " with the following extras: ")
for extra in orderedCar['extras']:
    print("\t" + extra)