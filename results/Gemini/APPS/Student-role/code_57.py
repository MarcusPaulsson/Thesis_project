def solve():
    n = int(input())
    f = list(map(int, input().split()))

    assigned = [False] * (n + 1)
    for i in range(n):
        if f[i] != 0:
            assigned[f[i]] = True

    unassigned_givers = []
    unassigned_receivers = []
    for i in range(n):
        if f[i] == 0:
            unassigned_givers.append(i)

    for i in range(1, n + 1):
        if not assigned[i]:
            unassigned_receivers.append(i)

    for i in range(len(unassigned_givers)):
        f[unassigned_givers[i]] = unassigned_receivers[i]

    
    for i in range(n):
        if f[i] == i + 1:
            for j in range(n):
                if i != j and f[j] != j + 1 and f[j] != 0:
                    f[i], f[j] = f[j], f[i]
                    break
            else:
                for j in range(n):
                    if i != j and f[j] != j + 1:
                        f[i], f[j] = f[j], f[i]
                        break
    
    for i in range(n):
        if f[i] == i + 1:
            for j in range(n):
                if i != j and f[j] != j + 1:
                    f[i], f[j] = f[j], f[i]
                    break

    print(*f)

solve()