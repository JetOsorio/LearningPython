def booksAvailable(books):
    for book in books:
        booksInStock = "The following title is available to buy " + book.title() + "."
        print(booksInStock)


available = ['elon musk', 'the everything store', 'the da vinci code']
booksAvailable(available)
