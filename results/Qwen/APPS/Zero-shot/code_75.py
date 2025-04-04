def max_days(a, b, c):
    return max(a + b + c, a + b, b + c, a + c)

a, b, c = map(int, input().split())
print(max_days(a, b, c))