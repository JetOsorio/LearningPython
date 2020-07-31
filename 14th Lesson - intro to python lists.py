# Lists are a collection of items
months = ['january', 'february', 'march', 'april']
print(months)  # Prints all items in list

print(months[0])  # Prints the month in position 0, the first item

print(months[0].title())
print(months[3].lower())

message = "I was born in " + months[2].title() + "."
print(message)