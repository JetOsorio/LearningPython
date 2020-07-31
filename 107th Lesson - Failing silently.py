def word_count(filename):
    # Count number of words in file
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
        # message = "Sorry, the file " + filename.title() + " cannot be found."
        # print(message)
    else:
        words = contents.split()
        number_words = len(words)
        print("The file " + filename.title() + " has approximately " + str(number_words) + " words")


filenames = ['programming', 'movies_line_by_line', 'bob ross'] #exception gets ignored
for filename in filenames:
    word_count(filename)
