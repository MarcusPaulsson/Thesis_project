def minimum_traps(m, x):
    # The number of traps needed is m // gcd(x, m)
    # Since gcd(x, m) = 1, we can directly return m - 1
    return m - 1

m, x = map(int, input().split())
print(minimum_traps(m, x))