def solve():
    n = int(input())
    f = list(map(int, input().split()))

    givers = []
    receivers = []
    assigned = [False] * (n + 1)

    for i in range(n):
        if f[i] != 0:
            assigned[f[i]] = True
        else:
            givers.append(i)

    for i in range(1, n + 1):
        if not assigned[i]:
            receivers.append(i)

    for i in range(len(givers)):
        f[givers[i]] = receivers[i]

    for i in range(n):
        if f[i] == i + 1:
            for j in range(len(givers)):
                if givers[j] != i:
                    f[i], f[givers[j]] = f[givers[j]], f[i]
                    break
            else:
                for j in range(n):
                    if j != i:
                        if f[j] != j + 1:
                            f[i], f[j] = f[j], f[i]
                            break

    print(*f)

solve()