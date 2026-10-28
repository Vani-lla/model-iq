import re

def fizz_buzz(n: int) -> int:
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            count += len(re.findall('7', str(i)))
    return count
