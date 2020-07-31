# in 'or' statement, tests need to satisfy at least one of the conditions
age = input("How old are you? ")
friendAge = input("How old is your friend? ")

if int(age) >= 18 or int(friendAge) >= 18:  # int(variable) is another way to convert string into int
    print("One of you is old enough to vote!")
else:
    print("Both of you are too young to vote.")
