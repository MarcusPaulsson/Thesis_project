def can_reach(n, m, d, c):
    if sum(c) == n:
        return "YES", [0] * (n - 1) + [1]
    if sum(c) < n:
        return "NO", []

n, m, d = map(int, input().split())
c = list(map(int, input().split()))
result, a = can_reach(n, m, d, c)
print(result)
if result == "YES":
    print(*a)