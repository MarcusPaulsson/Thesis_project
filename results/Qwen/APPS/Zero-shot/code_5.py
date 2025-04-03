n, pos, l, r = map(int, input().split())
print(max(pos - l, r - pos) + (n - r - 1) + (l - 1))