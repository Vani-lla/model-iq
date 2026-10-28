import re

def is_bored(S):
    sentences = re.split(r'[.?!]', S)
    boredom_count = sum(1 for sentence in sentences if sentence.strip().startswith('I '))
    return boredom_count