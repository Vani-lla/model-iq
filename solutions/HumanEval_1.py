from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(' ', '')
    result = []
    stack = []
    current = ''

    for char in paren_string:
        if char == '(':
            stack.append(char)
            current += char
        elif char == ')':
            stack.pop()
            current += char
            if not stack:
                result.append(current)
                current = ''

    return result
