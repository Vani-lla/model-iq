import re

def how_many_times(string: str, substring: str) -> int:
    return len(re.findall(f'(?={substring})', string))
