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
        giver_index = unassigned_givers[i]
        
        receiver = unassigned_receivers[i]
        
        if giver_index + 1 == receiver:
            
            if i + 1 < len(unassigned_givers):
                
                f[giver_index] = unassigned_receivers[i+1]
                f[unassigned_givers[i+1]] = receiver
                unassigned_receivers[i], unassigned_receivers[i+1] = unassigned_receivers[i+1], unassigned_receivers[i]
            else:
                
                
                
                temp = unassigned_receivers[0]
                f[giver_index] = temp
                f[unassigned_givers[0]] = receiver
                unassigned_receivers[0] = receiver
                
                
                
                
        else:
             f[giver_index] = receiver
           
    print(*f)

solve()