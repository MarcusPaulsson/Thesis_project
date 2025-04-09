def solve():
    n = int(input())
    f = list(map(int, input().split()))

    givers = [i + 1 for i in range(n)]
    receivers = [i + 1 for i in range(n)]

    given = set()
    received = set()

    for i in range(n):
        if f[i] != 0:
            given.add(f[i])

    missing_givers = []
    for i in range(n):
        if f[i] == 0:
            missing_givers.append(i)

    missing_receivers = []
    for i in range(1, n + 1):
        if i not in given:
            missing_receivers.append(i)

    for i in range(len(missing_givers)):
        f[missing_givers[i]] = missing_receivers[i]

    
    
    for i in range(len(missing_givers)):
        if f[missing_givers[i]] == missing_givers[i] + 1:
            
            for j in range(len(missing_givers)):
                if i != j and f[missing_givers[j]] != missing_givers[j] + 1:
                    f[missing_givers[i]], f[missing_givers[j]] = f[missing_givers[j]], f[missing_givers[i]]
                    break
            else:
                
                if len(missing_givers) > 1:
                  if i == 0:
                    f[missing_givers[i]], f[missing_givers[i+1]] = f[missing_givers[i+1]], f[missing_givers[i]]
                  else:
                    f[missing_givers[i]], f[missing_givers[0]] = f[missing_givers[0]], f[missing_givers[i]]

    print(*f)

solve()