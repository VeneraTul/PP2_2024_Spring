def is_prime(n):
    if n <= 1 or n % 2 == 0:
        return False     
    else:
        for i in range(2, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = filter_prime(numbers)
print(prime_numbers)


