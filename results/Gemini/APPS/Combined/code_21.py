def solve():
    n = int(input())
    a = list(map(int, input().split()))

    min_index = a.index(1)
    max_index = a.index(n)

    max_distance = max(min_index, max_index, n - 1 - min_index, n - 1 - max_index)

    print(max_distance)

solve()