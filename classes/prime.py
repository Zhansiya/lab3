numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 18, 19, 20]

is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))

prime_numbers = list(filter(is_prime, numbers))

print("Prime numbers:", prime_numbers)
