balance = input("What is your bank balance? ")
# 'elif' is equivalent to else if statement
if int(balance) <= 0:
    print("Would you like to make a deposit? ")
elif int(balance) <= 50:
    print("You don't qualify for interest.")
elif int(balance) < 100:  # can put multiple 'elif' statements
    print("Your interest rate is 1%")
else:  # 'elif' statement doesn't need to end on else statement
    print("Your interest rate is 2%")
