prompt = "\nTo end program, enter 'q'"
prompt += "\nPlease enter your name: "
message = " "
while message != 'q':
    message = input(prompt)
    print(message)