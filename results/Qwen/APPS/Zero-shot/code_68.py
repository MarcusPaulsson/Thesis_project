def min_cost(n, k, s):
    unique_chars = len(set(s))
    if k > 2**unique_chars:
        return -1
    return n * (k - 1)

n, k = map(int, input().split())
s = input()
print(min_cost(n, k, s))