def fruit_distribution(s, n):
    words = s.split()
    apples = int(words[0])
    oranges = int(words[3])
    mangoes = n - apples - oranges
    return mangoes