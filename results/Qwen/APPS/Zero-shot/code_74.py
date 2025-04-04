def min_cost(n, k, s):
    if k > 2**n:
        return -1
    return n * (2**n - k)

n, k = map(int, input().split())
s = input()
print(min_cost(n, k, s))