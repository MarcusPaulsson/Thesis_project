def max_distance(n, a):
    min_pos = a.index(1)
    max_pos = a.index(n)
    return max(min_pos, n - max_pos - 1)

n = int(input())
a = list(map(int, input().split()))
print(max_distance(n, a))