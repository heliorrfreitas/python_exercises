import string

def is_pangram(sentence):
    alphabet = list(string.ascii_lowercase)

    for letter in alphabet:
        if letter not in sentence.lower():
            return False

    return True
