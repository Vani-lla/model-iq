import collections

def search(lst):
    freq = collections.Counter(lst)
    for num in sorted(freq, reverse=True):
        if freq[num] >= num:
            return num
    return -1