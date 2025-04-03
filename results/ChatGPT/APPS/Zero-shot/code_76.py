t = int(input())
for _ in range(t):
    n = int(input())
    if n % 4 == 0 or n % 4 == 2:
        print("YES")
    else:
        print("NO")