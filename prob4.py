numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

filtered_squared = list(map(lambda x: x ** 2, filter(lambda x: x % 3 == 0, numbers)))

print(filtered_squared)
