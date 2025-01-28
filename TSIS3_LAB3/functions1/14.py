# 14. Create a python file and import some of the functions from the above 13 tasks and try to use them.
from itertools import permutations
import random

def grams_to_ounces(grams):
    return 28.3495231 * grams

def fahrenheit_to_centigrade(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return None, None

def filter_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    return [num for num in numbers if is_prime(num)]
        
def print_permutations(string):
    perms = permutations(string)
    for perm in perms:
        print(''.join(perm))

def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

def sphere_volume(radius):
    return (4 / 3) * 3.14159 * (radius ** 3)

def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def is_palindrome(word):
    cleaned_word = ''.join(filter(str.isalnum, word)).lower()
    return cleaned_word == cleaned_word[::-1]

def histogram(lst):
    for value in lst:
        print('*' * value)

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    guesses = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break

if __name__ == "__main__":
    print("--- Task Examples ---")

    # 1. Example
    print("100 grams to ounces:", grams_to_ounces(100))

    # 2. Example
    print("100F to Celsius:", fahrenheit_to_centigrade(100))

    # 3. Example
    print("Chickens and Rabbits:", solve(35, 94))

    # 4. Example
    print("Prime numbers:", filter_prime([2, 3, 4, 5, 6, 7, 8, 9, 10]))

    # 5. Example
    print("Permutations of 'abc':")
    print_permutations('abc')

    # 6. Example
    print("Reversed words:", reverse_words("We are ready"))

    # 7. Example
    print("Has 33:", has_33([1, 3, 3]))

    # 8. Example
    print("Spy game:", spy_game([1, 2, 4, 0, 0, 7, 5]))

    # 9. Example
    print("Volume of sphere (radius 3):", sphere_volume(3))

    # 10. Example
    print("Unique elements:", unique_elements([1, 2, 2, 3, 4, 4, 5]))

    # 11. Example
    print("Is palindrome 'madam':", is_palindrome("madam"))

    # 12. Example
    print("Histogram:")
    histogram([4, 9, 7])

    # 13. Example
    guess_the_number()