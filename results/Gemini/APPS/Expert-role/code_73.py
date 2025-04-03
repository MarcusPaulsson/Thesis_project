def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    ops = []
    
    def get_mex(arr):
        seen = set(arr)
        for i in range(n + 1):
            if i not in seen:
                return i
        return n + 1 
    
    for _ in range(2 * n):
        
        is_sorted = all(a[i] <= a[i+1] for i in range(n-1))
        if is_sorted:
            break
        
        mex = get_mex(a)
        
        if mex < n:
            
            for i in range(n):
                if a[i] != i:
                    a[i] = mex
                    ops.append(i + 1)
                    break
        else:
            for i in range(n -1, -1, -1):
                if not all(a[j] <= a[j+1] for j in range(n-1)):
                    
                    for k in range(n-1):
                        if a[k] > a[k+1]:
                            a[k] = mex
                            ops.append(k+1)
                            break
                    break
            
    print(len(ops))
    print(*ops)
    

t = int(input())
for _ in range(t):
    solve()