import heapq

def strange_sort_list(lst):
    if not lst:
        return []
    result = []
    while lst:
        result.append(heapq.heappop(lst))  # Get the minimum
        if lst:
            result.append(lst.pop())  # Get the maximum
    return result