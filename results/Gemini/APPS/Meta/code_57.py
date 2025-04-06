def solve():
    n = int(input())
    f = list(map(int, input().split()))

    givers = [i + 1 for i in range(n)]
    receivers = [True] * (n + 1)
    receivers[0] = False

    for i in range(n):
        if f[i] != 0:
            receivers[f[i]] = False

    available_receivers = []
    for i in range(1, n + 1):
        if receivers[i]:
            available_receivers.append(i)
    
    unknown_givers_indices = []
    for i in range(n):
        if f[i] == 0:
            unknown_givers_indices.append(i)

    for i in range(len(unknown_givers_indices)):
        f[unknown_givers_indices[i]] = available_receivers[i]

    # Handle self-gifting
    for i in range(n):
        if f[i] == i + 1:
            for j in range(n):
                if i != j and f[j] != 0 and f[j] != j + 1:
                  
                  temp = f[i]
                  f[i] = f[j]
                  f[j] = temp
                  break
            else:
                for j in range(n):
                  if i != j and f[j] == 0:
                    if i + 1 != available_receivers[unknown_givers_indices.index(j)] and j+1 != available_receivers[unknown_givers_indices.index(i)]:
                      temp = f[i]
                      f[i] = f[j]
                      f[j] = temp
                      break
                else:
                   
                    for j in range(n):
                       if j != i:
                            temp = f[i]
                            f[i] = f[j]
                            f[j] = temp
                            if f[i] == i + 1 or f[j] == j+1:
                                temp = f[i]
                                f[i] = f[j]
                                f[j] = temp
                            break


    print(*f)

solve()