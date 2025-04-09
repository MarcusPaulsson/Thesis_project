def solve():
    n = int(input())
    f = list(map(int, input().split()))

    givers = list(range(1, n + 1))
    receivers = list(range(1, n + 1))

    for i in range(n):
        if f[i] != 0:
            if f[i] in givers:
                givers.remove(f[i])
            if i + 1 in receivers:
                receivers.remove(i + 1)

    zeros_indices = [i for i in range(n) if f[i] == 0]

    for i in range(len(zeros_indices)):
        idx = zeros_indices[i]
        
        possible_receivers = []
        for r in receivers:
            if r != idx + 1:
                possible_receivers.append(r)
                
        if not possible_receivers:
            for r in receivers:
              if r == idx+1:
                continue
        
        f[idx] = possible_receivers[0]
        receivers.remove(possible_receivers[0])

    print(*f)

solve()