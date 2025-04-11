def solve():
    n = int(input())
    f = list(map(int, input().split()))

    givers = []
    receivers = []

    assigned = [False] * (n + 1)
    for i in range(n):
        if f[i] != 0:
            assigned[f[i]] = True

    for i in range(n):
        if f[i] == 0:
            givers.append(i)

    for i in range(1, n + 1):
        if not assigned[i]:
            receivers.append(i)

    for i in range(len(givers)):
        if givers[i] == receivers[i] - 1:
            if i + 1 < len(givers):
                receivers[i], receivers[i+1] = receivers[i+1], receivers[i]
            else:
                receivers[i], receivers[i-1] = receivers[i-1], receivers[i]

    for i in range(len(givers)):
        f[givers[i]] = receivers[i]

    print(*f)

solve()