n = int(input())
a = list(map(int, input().split()))

min_a = min(a)
max_a = max(a)

if min_a == max_a:
    print(0)
else:
    diff = max_a - min_a
    if (diff % 2) == 0:
        D = diff // 2
        print(D)
    else:
        print(-1)