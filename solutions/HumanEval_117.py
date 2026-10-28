import re

def select_words(s, n):
    if not s:
        return []

    words = s.split()
    result = []

    for word in words:
        consonants = re.findall(r'[bcdfghjklmnpqrstvwxyz]', word, re.IGNORECASE)
        if len(consonants) == n:
            result.append(word)

    return result