inStock = ['blue pens', 'paper', 'staples']
shoppingCart = ['blue pens', 'paper', 'staples', 'orange post-its']

for item in shoppingCart:
    if item in inStock:
        print("Adding " + item + " to your order.")
    else:
        print("Sorry, " + item + "is not in stock")
print("Your order is complete")