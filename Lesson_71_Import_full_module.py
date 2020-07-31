def books_available(*books):
    for book in books:
        books_in_stock = 'The following title is available to read: ' + book
        print(books_in_stock)


# For lesson 72
def book_description(author_name, book_type="non-fiction"):
    print("This is a " + book_type + " book.")
    print("The author of this book is " + author_name.title())
