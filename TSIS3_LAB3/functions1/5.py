# 5. Write a function that accepts string from user and print all permutations of that string.
from itertools import permutations

def print_permutations(string):
    perms = permutations(string)
    for perm in perms:
        print(''.join(perm))
