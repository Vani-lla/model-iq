import collections

def histogram(test):
    if not test:
        return {}

    # Split the input string into a list of letters
    letters = test.split()

    # Count the occurrences of each letter
    letter_counts = collections.Counter(letters)

    # Find the maximum occurrence count
    max_count = max(letter_counts.values(), default=0)

    # Filter letters that have the maximum occurrence count
    result = {letter: count for letter, count in letter_counts.items() if count == max_count}

    return result