message = input("What is your favourite film? ")
print(message.title())

filename =  'favorite_film'

with open(filename, 'a') as file_object:
    file_object.write(message + "\n")