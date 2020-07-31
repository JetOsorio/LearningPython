book1 = {'title' : 'diary of the wimpy kid', 'author': 'jeff kinney', 'price' : '11.99'}
book2 = {'title' : 'captain underpants', 'author': 'dave pikley', 'price' : '10.99'}
book3 = {'title' : 'road warrior', 'author' : 'rimjob bob', 'price' : '99.99'}

books = [book1, book2, book3]

for book in books:
    print(book)

#Make 50 blue pens
stockItems = []
for bluePen in range(0, 50):
    newBluePen = {'colour': 'blue', 'type' : 'ballpoint', 'price': '0.50'}
    stockItems.append(newBluePen)
#Changing price of first 5 pens
for bluePen in stockItems[0:5]:
    if bluePen['price'] == '0.50':
        bluePen['price'] = '0.25'

for bluePen in stockItems[0:5]:
    print(bluePen)


print(stockItems)