filename = input("Input file name: ")

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    message = "Sorry, the file " + filename + " cannot be found."
    print(message)
else:
    words = contents.split()
    number_words = len(words)
    print("The file " + filename + " has approximately " + str(number_words) + " words")

