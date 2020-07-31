prompt = '\nPlease enter name of book you have read recently'
prompt += "\nTo quit type 'q'."

while True:
    book = input(prompt)

    if book == 'q':
        break  # stops 'while' loop
    else:
        print("You have recently read " + book.title())
