username = input("Welcome, please enter username. ")
password = input("Please enter your password. ")
# 'and' condition ensure both conditions need to be passed
if username != 'bob' and password != 'password':  # 'and' condition here does not work for some reason
    print("Access Denied.")
else:
    print("Welcome!")

if username == 'bob' and password == 'password':  # this 'and' condition works
    print("Welcome!")
else:
    print("Access Denied.")
