def solve():
    n = int(input())
    a = list(map(int, input().split()))

    def mex(arr):
        s = set(arr)
        for i in range(n + 1):
            if i not in s:
                return i
        return n + 1

    ops = []
    
    for i in range(n):
        if a[i] != i:
            m = mex(a)
            if m < n:
                ops.append(a.index(m) + 1)
                a[a.index(m)] = m
                
            else:
                ops.append(i + 1)
                a[i] = m

    for i in range(n):
        m = mex(a)
        ops.append(a.index(m)+1)
        a[a.index(m)] = m

    
    
    
    
    
    
    
    
    
    b = a[:]
    
    for i in range(len(ops)):
        b[ops[i]-1] = mex(b)
        
    
    
    
    
    print(len(ops[:n]))
    print(*ops[:n])

t = int(input())
for _ in range(t):
    solve()