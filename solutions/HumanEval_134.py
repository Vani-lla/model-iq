import re

def check_if_last_char_is_a_letter(txt):
    # Check if the last character is a letter and not part of a word
    return bool(re.search(r'\b[a-zA-Z]\b$', txt))