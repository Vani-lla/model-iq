import heapq

def next_smallest(lst):
    if len(lst) < 2:
        return None
    unique_elements = list(set(lst))
    if len(unique_elements) < 2:
        return None
    return heapq.nsmallest(2, unique_elements)[1]