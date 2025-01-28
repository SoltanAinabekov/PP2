# 4. Write a function `filter_prime` which will take list of numbers as an agrument and returns only prime numbers from the list.
def filter_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    return [num for num in numbers if is_prime(num)]
