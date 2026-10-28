import heapq

def maximum(arr, k):
    return sorted(heapq.nlargest(k, arr))