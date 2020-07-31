def buildBook(name, author, publisher):
    book = {'name': name, 'author': author, 'publisher': publisher}
    return book


myBook = buildBook('elon musk', 'ashlee vance', 'virgin books')
print(myBook)
