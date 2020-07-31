terms = {'variable': 'represents or refers to a value stored in a memory', 'string': 'a sequence of characters'}

if 'float' in terms:
    print("I know what a float is.")
else:
    print('I do not know what that is.')

print(terms['variable'])

#Here is how to add items in dictionary
terms['float'] = 'Represents a decimal number'
terms['integer'] = 'A whole number.'

print(terms['float'])
print(terms['integer'])