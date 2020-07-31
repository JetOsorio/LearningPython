class Book():
    # A class to create a book
    def __init__(self, name, price, publisher):  # 'init' method is a special method that runs automatically based on
        # the class
        # 'self' parameter is always first
        # initialise the name, price and publisher attributes
        self.name = name
        self.price = price
        self.publisher = publisher

    def hardback(self):
        # Simulate a hardback book
        print(self.name.title() + " is a hardback book.")

    def softback(self):
        # Simulate a softback book
        print(self.name.title()) + " is a softback book."

    def ebook(self):
        # Simulate an ebook
        print(self.name.title() + " is an ebook.")

    def ebook_reader(self):
        #Simulate an ebook reader
        print("Library: " + self.name.title() + ", $" + str(self.price) + ", " + self.publisher.title() + ".")

# This is the instance of class 'Book'
my_Book = Book('elon musk', 14.99, 'virgin books')
your_book = Book('the everything store', 9.99, 'virgin books')

#Calling our ebook reader method
my_Book.ebook_reader()
#Second instance
your_book.hardback()