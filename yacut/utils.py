from random import choice
from string import ascii_letters, digits


def get_unique_short_id(length):
    letters = ascii_letters + digits
    return ''.join(choice(letters) for i in range(length))
