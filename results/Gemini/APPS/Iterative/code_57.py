def solve():
    n = int(input())
    f = list(map(int, input().split()))

    assigned = [False] * (n + 1)
    for i in range(n):
        if f[i] != 0:
            assigned[f[i]] = True

    unassigned_givers = []
    for i in range(n):
        if f[i] == 0:
            unassigned_givers.append(i)

    unassigned_receivers = []
    for i in range(1, n + 1):
        if not assigned[i]:
            unassigned_receivers.append(i)

    for i in range(len(unassigned_givers)):
        giver_index = unassigned_givers[i]
        receiver = unassigned_receivers[i]

        f[giver_index] = receiver

    # Check for self-gifting and swap if necessary
    for i in range(n):
        if f[i] == i + 1:
            # Find another index to swap with
            for j in range(n):
                if i != j and f[j] != j + 1 and f[j] != 0 and f[j] != i + 1:
                    f[i], f[j] = f[j], f[i]
                    break
            else:
                # If no suitable j is found, swap with the next unassigned giver
                for j in range(len(unassigned_givers)):
                    giver_index = unassigned_givers[j]
                    if giver_index != i:
                        f[i], f[giver_index] = f[giver_index], f[i]
                        break
                else:
                    # If still no suitable swap, find any other index
                    for j in range(n):
                        if i != j:
                            f[i], f[j] = f[j], f[i]
                            break
    
    print(*f)

solve()