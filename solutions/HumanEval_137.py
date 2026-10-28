import re

def compare_one(a, b):
    # Convert strings to floats if necessary
    if isinstance(a, str):
        a = re.sub(r',', '.', a)
        a = float(a)
    if isinstance(b, str):
        b = re.sub(r',', '.', b)
        b = float(b)

    # Compare the values
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None