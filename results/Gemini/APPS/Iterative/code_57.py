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
        f[givers[i]] = receivers[i]

    for i in range(n):
        if f[i] == i + 1:
            for j in range(n):
                if i != j and f[j] != j + 1:
                    f[i], f[j] = f[j], f[i]
                    break
            else:
                for k in range(1, n + 1):
                    if k != i + 1 and k not in f:
                        f[i] = k
                        break

    print(*f)

solve()