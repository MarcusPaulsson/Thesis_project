n = int(input())
a = list(map(int, input().split()))

min_a = min(a)
max_a = max(a)

if min_a == max_a:
    print(0)
else:
    D = (max_a - min_a) // 2
    if (max_a - min_a) % 2 == 0:
        print(D)
    else:
        print(-1)