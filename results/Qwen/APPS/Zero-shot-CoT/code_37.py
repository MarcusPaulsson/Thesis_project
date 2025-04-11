a, b, c = map(int, input().split())
if c % gcd(a, b) == 0:
    print("Yes")
else:
    print("No")