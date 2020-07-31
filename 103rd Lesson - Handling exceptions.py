print("Please enter two numbers to be divided? ")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break

    second_number = input("Second Number:")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
        
    if second_number == 'q':
        break