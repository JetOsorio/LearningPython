numbers = list(range(1, 6))  # Creates list of numbers [1, 2, 3, 4, 5]
print(numbers)

oddNumbers = list(range(1, 101, 2))  # Adds 2 to each number, starting at 1 until 101
print(oddNumbers)

squares = []
for value in range(1, 11):
    square = value ** 2  # multiplies each number in range with exponent 2
    squares.append(square)  # empty square list is filled with square value
print(squares)

digits = [1, 2, 3, 4, 5]
print(min(digits))  # finds smallest number in list
print(max(digits))  # finds biggest number in list
print(sum(digits))  # adds up all numbers in list
