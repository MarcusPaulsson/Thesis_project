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
                    
                    if len(unassigned_receivers) == 1:
                        
                        for k in range(n):
                            if f[k] == unassigned_receivers[0] and k != i :
                                temp = f[k]
                                f[k] = f[i]
                                f[i] = temp
                                break
                    else:
                        idx = unassigned_receivers.index(f[i])
                    
                        temp = f[unassigned_givers[(j+1)% len(unassigned_givers)]]
                        
                        f[unassigned_givers[(j+1)% len(unassigned_givers)]] = f[i]
                        f[i] = temp
                        break

    print(*f)

solve()