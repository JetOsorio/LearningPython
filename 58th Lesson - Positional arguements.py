def bookDescription(bookType, authorName):
    print("\nThis book is " + bookType + ".")
    print("The author of this book is " + authorName.title() + ".")


bookDescription('non-fiction', 'ashlee vance')
bookDescription('fiction', 'dan brown')
