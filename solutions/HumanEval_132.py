import re

def is_nested(string):
    stack = []
    nested = False
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']' and stack:
            stack.pop()
            if stack:
                nested = True
    return nested
