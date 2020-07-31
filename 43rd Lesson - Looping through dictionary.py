birthdayMonths = {'bob': 'march', 'wilby': 'may', 'john': 'december', 'karen': 'november'}

for x, y in birthdayMonths.items():
    print("\nName: " + x)
    print("Month: " + y)

book1 = {
    'name' : 'Captain Underpants',
    'author': 'david pikley',
    'price' : '9.99'
}

for key, value in book1.items(): #'key' and 'value' can be named any variable
    print("\nKey: " + key)
    print("Value: " + value)
