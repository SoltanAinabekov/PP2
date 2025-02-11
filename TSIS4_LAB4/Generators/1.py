# Create a generator that generates the squares of numbers up to some number N.
def square_generator(N):
    for i in range(N + 1):
        yield i ** 2

N = 10
for num in square_generator(N):
    print(num, end=" ")
    