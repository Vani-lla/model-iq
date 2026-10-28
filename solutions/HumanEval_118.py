import re

def get_closest_vowel(word):
    vowels = 'aeiouAEIOU'
    # Use regex to find all vowels that are between consonants
    matches = re.findall(r'(?<=[^aeiouAEIOU])[aeiouAEIOU](?=[^aeiouAEIOU])', word)
    if matches:
        return matches[-1]
    else:
        return ''