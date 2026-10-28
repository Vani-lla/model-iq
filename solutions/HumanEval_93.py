import string

def encode(message):
    vowels = 'aeiou'
    shifted_vowels = {v: chr((ord(v) - ord('a') + 2) % 26 + ord('a')) for v in vowels}
    shifted_vowels.update({v.upper(): shifted_vowels[v].upper() for v in shifted_vowels})
    encoded_message = ''.join(shifted_vowels.get(c, c) for c in message)
    return encoded_message.swapcase()