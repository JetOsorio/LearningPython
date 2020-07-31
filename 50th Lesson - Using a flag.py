prompt = "\nEnter 'q' to end this program."
prompt += "\nWhat is your name? "

#set flag to true
active = True
while active:
    message = input(prompt)

    if message == 'q':
        active = False
    else:
        print(message)