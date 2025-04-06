def solve():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    
    used = set(p)
    remaining = []
    for i in range(n, 0, -1):
        if i not in used:
            remaining.append(i)
    
    p += remaining
    
    def is_stack_sortable(arr):
        s = []
        b = []
        a = arr[:]
        
        i = 0
        while i < 2 * n:
            if len(a) > 0:
                if len(s) == 0 or a[0] < s[-1]:
                    s.append(a.pop(0))
                    i += 1
                else:
                    if len(s) > 0:
                        b.append(s.pop())
                        i += 1
                    else:
                        return False
            else:
                if len(s) > 0:
                    b.append(s.pop())
                    i += 1
                else:
                    break

        if len(s) > 0:
            
            return False
        
        for i in range(len(b) - 1):
            if b[i] > b[i+1]:
                
                return False
        return True
        
    
    
    
    if is_stack_sortable(p):
        print(*p)
    else:
        print(-1)
    

solve()