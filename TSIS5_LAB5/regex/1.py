# Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re

def match_a_b(string):
    pattern = r'^a*b*$'
    return bool(re.fullmatch(pattern, string))

print(match_a_b("a")) 
print(match_a_b("ab"))   
print(match_a_b("b"))       