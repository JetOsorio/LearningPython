shoppingCart = ['pens', 'paper', 'stapler', 'post-its']

#IF statements with lists
for item in shoppingCart:
    if item == 'pens':
        print("Sorry, that item, " + item + ", is out of stock.")
    else:
        print("Adding " + item + " to your order.")

print("Your order is complete.")

# Working with empty lists
shoppingCart2 = ['pens']

if shoppingCart2:
    for item in shoppingCart2:
        print("Adding " + item + " to your cart.")
    print("Your order is complete.")
else:
    print("You must select an item before proceeding")