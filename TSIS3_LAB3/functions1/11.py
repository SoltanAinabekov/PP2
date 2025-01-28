# 11. Write a Python function that checks whether a word or phrase is `palindrome` or not. Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam.
def is_palindrome(word):
    cleaned_word = ''.join(filter(str.isalnum, word)).lower()
    return cleaned_word == cleaned_word[::-1]
