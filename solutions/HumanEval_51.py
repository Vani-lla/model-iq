import re

def remove_vowels(text):
    vowels = 'aeiouAEIOU'
    return re.sub(f'[{vowels}]', '', text)