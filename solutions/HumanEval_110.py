import collections


def exchange(lst1, lst2):
    # Count the number of odd numbers in lst1
    odd_count = collections.Counter(lst1)['odd']

    # Count the number of even numbers in lst2
    even_count = collections.Counter(lst2)['even']

    # If there are enough even numbers in lst2 to exchange with all odd numbers in lst1, return 'YES'
    if even_count >= odd_count:
        return 'YES'
    else:
        return 'NO'
