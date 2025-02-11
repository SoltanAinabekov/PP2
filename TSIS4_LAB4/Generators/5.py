# Implement a generator that returns all numbers from (n) down to 0.
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = 10
for num in countdown(n):
    print(num, end=" ")
    