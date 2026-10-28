import re

def solve(s):
    if re.search('[a-zA-Z]', s):
        return ''.join(c.swapcase() if c.isalpha() else c for c in s)
    else:
        return s[::-1]