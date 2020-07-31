age = 18
if age == 18:
    print('True')
else:
    print('False')

raw_age2 = input("How old are you? ")  # Not part of lesson, but good to know
age2 = int(raw_age2)  # converts string into integer
if age2 < 18:  # error would occur if age2 was not an integer
    print("You're a minor")
else:
    print("You're an adult")
