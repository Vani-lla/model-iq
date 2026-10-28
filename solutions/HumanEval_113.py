import re

def odd_count(lst):
    result = []
    for s in lst:
        odd_count = len(re.findall(r'[13579]', s))
        result.append(f"the number of odd elements {odd_count}n the str{odd_count}ng {odd_count} of the {odd_count}nput.")
    return result