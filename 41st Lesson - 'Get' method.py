terms = {'integer' : 'A whole number'}

print(terms.get('integer'))
print(terms.get('float', 'Not in the dictionary')) # if default message not supplied (the message next to float) error occurs
