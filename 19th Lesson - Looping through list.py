months = ['january', 'feburary', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november',
          'december']

# for loop allows for repeated tasks
for month in months:  # month = each item in 'months' list
    print(month.title() + " is the name of a month") # indented line following for loop counts as being a part of loop

for month in months:
    print(month.title() + "\n")
    print("The next month is")
