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
            for j in range(len(unassigned_givers)):
                if unassigned_givers[j] == i:
                    if j > 0:
                        f[unassigned_givers[j]], f[unassigned_givers[j-1]] = f[unassigned_givers[j-1]], f[unassigned_givers[j]]
                    else:
                        if len(unassigned_givers) > 1:
                            f[unassigned_givers[j]], f[unassigned_givers[j+1]] = f[unassigned_givers[j+1]], f[unassigned_givers[j]]
                        else:
                            for k in range(n):
                                if k != i and f[k] != 0 and f[k] != i+1:
                                    temp = f[k]
                                    f[k] = f[i]
                                    f[i] = temp
                                    break
                    break
    
    for i in range(n):
        if f[i] == i + 1:
            for k in range(n):
                if k != i and f[k] != 0 and f[k] != i+1:
                    temp = f[k]
                    f[k] = f[i]
                    f[i] = temp
                    break
    
    print(*f)

solve()