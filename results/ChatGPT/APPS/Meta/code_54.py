n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(0)
else:
    min_a = min(a)
    max_a = max(a)

    if max_a == min_a:
        print(0)
    elif (max_a - min_a) % 2 == 0:
        D = (max_a - min_a) // 2
        print(D)
    else:
        print(-1)