subscribers = ['osoriojet@gmail.com', 'powerjet@y7mail.com', 'fakeemail@hotmail.com']
print(subscribers)

poppedSubscribers = subscribers.pop()  # removes last item from list, but allows item to be used after removal
print(subscribers)
print(poppedSubscribers)

subscribers = ['osoriojet@gmail.com', 'powerjet@y7mail.com', 'fakeemail@hotmail.com']
firstSub = subscribers.pop(0) # removes item in first index, but is then used as variable
print(subscribers)
print("Your first subscriber was " + firstSub + ".")

subscribers = ['osoriojet@gmail.com', 'powerjet@y7mail.com', 'fakeemail@hotmail.com']
print(subscribers)
subscribers.remove('powerjet@y7mail.com') # remove method discards first matching value, not a specific index
print(subscribers)

subscribers = ['osoriojet@gmail.com', 'powerjet@y7mail.com', 'fakeemail@hotmail.com']
subscribed_by_mistake = 'powerjet@y7mail.com'
subscribers.remove(subscribed_by_mistake)
print(subscribers)
print("This person, " + subscribed_by_mistake + ", did not mean to sign up")