def solve():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    used = set(p)
    remaining = []
    for i in range(n, 0, -1):
        if i not in used:
            remaining.append(i)

    p = p + remaining
    
    def is_stack_sortable(arr):
        a = arr[:]
        s = []
        b = []
        
        i = 0
        j = 0
        
        while i < len(arr) or len(s) > 0:
            
            if len(s) > 0 and (i == len(arr) or s[-1] < (arr[i] if i < len(arr) else float('inf'))):
                b.append(s.pop())
            elif i < len(arr):
                s.append(arr[i])
                i += 1
            else:
                return False
                
        for i in range(len(b) - 1):
            if b[i] > b[i+1]:
                return False
        return True

    
    used = set(p[:k])
    remaining = []
    for i in range(n, 0, -1):
        if i not in used:
            remaining.append(i)
    
    
    best_p = None
    
    import itertools
    
    for perm in itertools.permutations(remaining):
        temp_p = p[:k] + list(perm)
        
        if is_stack_sortable(temp_p):
            if best_p is None:
                best_p = temp_p
            else:
                if temp_p > best_p:
                    best_p = temp_p
    
    if best_p is None:
        print("-1")
    else:
        print(*best_p)

solve()