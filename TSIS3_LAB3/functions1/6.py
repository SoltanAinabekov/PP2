# 6. Write a function that accepts string from user, return a sentence with the words reversed.
def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])
