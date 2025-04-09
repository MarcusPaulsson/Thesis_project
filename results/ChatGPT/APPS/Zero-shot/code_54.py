n = int(input())
a = list(map(int, input().split()))

min_a = min(a)
max_a = max(a)

if n == 1:
    print(0)
else:
    if max_a - min_a > 2 * (max_a - min_a) // 2:
        print(-1)
    else:
        D = (max_a - min_a) // 2
        print(D)