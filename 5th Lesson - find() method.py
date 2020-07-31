# find() looks for the string and counts which the number of characters before start of word [includes spaces]
favBook = "My favourite book is 'Twilight'.".find('Twilight') #Case sensitive
print(favBook) #if string not found, it prints -1

stuff = "@ me bro".find("@")
print(stuff) #Starts at 0