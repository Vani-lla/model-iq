import collections


def correct_bracketing(brackets: str) -> bool:
    stack = collections.deque()
    for bracket in brackets:
        if bracket == '<':
            stack.append(bracket)
        elif bracket == '>':
            if not stack:
                return False
            stack.pop()
    return not stack
