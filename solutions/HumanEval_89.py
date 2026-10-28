import string

def encrypt(s):
    alphabet = string.ascii_lowercase
    rotated_alphabet = alphabet[2 * 2:] + alphabet[:2 * 2]
    translation_table = str.maketrans(alphabet, rotated_alphabet)
    return s.translate(translation_table)