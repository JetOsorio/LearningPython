def bookDescription(authorName, bookType='non-fiction'):  # 'non-fiction' is the default value
    print("\nThis book is a " + bookType + ".")
    print('The author of this book is ' + authorName.title())


# default value parameters are typically positioned last
bookDescription('ashlee vance')
bookDescription('ashlee vance', bookType='fiction')  # default values can still be changed
