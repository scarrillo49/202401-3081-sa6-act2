numbers = [1, 2, 3, 4, 5, 6]

# Use filter() and lambda to find even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers) 