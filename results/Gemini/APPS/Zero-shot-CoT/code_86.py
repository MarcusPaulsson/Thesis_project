def solve():
    n = int(input())
    a = list(map(int, input().split()))

    zeros = a.count(0)
    ones = a.count(1)

    if zeros >= n // 2:
        print(zeros)
        print(*([0] * zeros))
    else:
        if ones % 2 == 0:
            print(ones)
            print(*([1] * ones))
        else:
            print(ones - 1)
            print(*([1] * (ones - 1)))

t = int(input())
for _ in range(t):
    solve()