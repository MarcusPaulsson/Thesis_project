read = lambda: list(map(int, input().split()))
n = int(input())
a = list(read())
x, y = a.index(1), a.index(n)
ans = max(x, y, n - x - 1, n - y - 1)
print(ans)
