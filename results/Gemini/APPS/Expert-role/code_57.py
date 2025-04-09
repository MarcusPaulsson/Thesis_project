def solve():
    n = int(input())
    f = list(map(int, input().split()))
    
    f_copy = f[:]
    
    assigned = [False] * n
    for val in f:
        if val != 0:
            assigned[val-1] = True
    
    unassigned = []
    for i in range(n):
        if f[i] == 0:
            unassigned.append(i)
    
    available = []
    for i in range(n):
        if not assigned[i]:
            available.append(i)
    
    for i in range(len(unassigned)):
        f[unassigned[i]] = available[i] + 1
        
    
    
    conflicts = []
    for i in range(n):
        if f[i] == i+1:
            conflicts.append(i)
            
    
    if len(conflicts) > 0:
        if len(conflicts) == 1:
            
            for i in range(n):
              if f_copy[i] == 0 and i != conflicts[0]:
                temp = f[conflicts[0]]
                f[conflicts[0]] = f[i]
                f[i] = temp
                break
        else:
            for i in range(0,len(conflicts)):
                temp = f[conflicts[i]]
                
                f[conflicts[i]] = f[conflicts[(i+1)%len(conflicts)]]
                f[conflicts[(i+1)%len(conflicts)]] = temp
                    
                    
                
    print(*f)

solve()