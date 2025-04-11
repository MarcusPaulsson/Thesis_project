def minimum_D(n, a):
    min_a = min(a)
    max_a = max(a)

    if min_a == max_a:
        return 0

    if (max_a - min_a) % 2 != 0:
        return -1

    D = (max_a - min_a) // 2
    return D

n = int(input())
a = list(map(int, input().split()))
print(minimum_D(n, a))