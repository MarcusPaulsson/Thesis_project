def solve():
    n = int(input())
    f = list(map(int, input().split()))

    givers = [i + 1 for i in range(n) if f[i] == 0]
    receivers = [i + 1 for i in range(1, n + 1) if i not in f]

    for i in range(len(givers)):
        if givers[i] == receivers[i]:
            if i + 1 < len(givers):
                receivers[i], receivers[i+1] = receivers[i+1], receivers[i]
            else:
                receivers[i], receivers[0] = receivers[0], receivers[i]

    for i in range(len(givers)):
        f[givers[i] - 1] = receivers[i]

    print(*f)

solve()