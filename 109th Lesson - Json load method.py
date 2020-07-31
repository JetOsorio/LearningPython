import json

phone_numbers = [1234567890]

filename = 'phone_number.json'
with open(filename) as file_object:
    phone_numbers = json.load(file_object)

print(phone_numbers)

