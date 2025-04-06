def solve():
    n = int(input())
    f = list(map(int, input().split()))

    givers = [i + 1 for i in range(n)]
    receivers = [i + 1 for i in range(n)]

    assigned_receivers = set()
    for i in range(n):
        if f[i] != 0:
            givers.remove(i + 1)
            receivers.remove(f[i])
            assigned_receivers.add(f[i])

    unassigned_givers_indices = [i for i in range(n) if f[i] == 0]

    for i in range(len(unassigned_givers_indices)):
        giver_index = unassigned_givers_indices[i]
        giver = giver_index + 1
        
        possible_receivers = []
        for receiver in receivers:
            if receiver != giver:
                possible_receivers.append(receiver)
        
        if not possible_receivers:
            print("No solution exists.")
            return

        receiver = possible_receivers[0]
        
        f[giver_index] = receiver
        receivers.remove(receiver)

    # Check for self-gifting after assigning initial values.
    for i in range(n):
        if f[i] == i + 1:
            # Swap with another unassigned index if possible
            for j in range(n):
                if i != j and f[j] != 0 and f[j] != j + 1:
                    if f[i] not in [k+1 for k in range(n) if k != j]:
                        
                        temp = f[i]
                        f[i] = f[j]
                        f[j] = temp
                        break
            else:
                # Swap with another unassigned index if possible
                for j in range(n):
                    if i != j and f[j] != 0 :
                        
                        temp = f[i]
                        f[i] = f[j]
                        f[j] = temp
                        break

    print(*f)

solve()