def solve():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    q = list(map(int, input().split()))

    prefix_sums = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sums[i] = prefix_sums[i - 1] + a[i - 1]

    for query in q:
        for i in range(1, n + 1):
            if query <= prefix_sums[i]:
                print(i)
                break

solve()