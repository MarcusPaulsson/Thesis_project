def solve():
    n = int(input())
    f = list(map(int, input().split()))
    
    givers = [i + 1 for i in range(n)]
    receivers = [i + 1 for i in range(n)]
    
    given = set()
    for val in f:
        if val != 0:
            given.add(val)
    
    not_given = []
    for i in range(1, n + 1):
        if i not in given:
            not_given.append(i)
            
    zeros = []
    for i in range(n):
        if f[i] == 0:
            zeros.append(i)
    
    for i in range(len(zeros)):
        f[zeros[i]] = not_given[i]
        
    
    
    
    
    
    
    
    conflicts = []
    for i in range(n):
        if f[i] == i + 1:
            conflicts.append(i)
            
    if len(conflicts) > 0:
        if len(conflicts) == 1:
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            for i in range(n):
                if i != conflicts[0] and f[i] != i + 1 and i+1 != f[conflicts[0]]:
                    temp = f[conflicts[0]]
                    f[conflicts[0]] = f[i]
                    f[i] = temp
                    
                    
                    break
        elif len(conflicts) > 1:
            
            
            
            
            for i in range(0,len(conflicts),2):
                if i+1 < len(conflicts):
                    temp = f[conflicts[i]]
                    f[conflicts[i]] = f[conflicts[i+1]]
                    f[conflicts[i+1]] = temp
                else:
                    
                    
                    
                    for j in range(n):
                        if j != conflicts[i] and f[j] != j+1 and j+1 != f[conflicts[i]]:
                            temp = f[conflicts[i]]
                            f[conflicts[i]] = f[j]
                            f[j] = temp
                            
                            break
            
    print(*f)

solve()