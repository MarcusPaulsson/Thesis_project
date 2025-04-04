a, b, c = map(int, input().split())
if c % a == 0 or c % b == 0 or (a + b) <= c:
    print("Yes")
else:
    print("No")