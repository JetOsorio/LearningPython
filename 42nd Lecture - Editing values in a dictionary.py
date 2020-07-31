terms = {'integer': 'Is a number that contains a decimal place', 'string' : 'a sequence of characters'}

terms["integer"] = 'A whole number' # This creates a new value but doesnt change old one
print(terms.get('integer'))

del terms['integer'] # deletes all values which are exactly 'integer'
print(terms)