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
        
        def can_sort(a, s, b):
            if not a and not s:
                for i in range(len(b) - 1):
                    if b[i] > b[i+1]:
                        return False
                return True
            
            if a:
                s_new = s[:]
                s_new.append(a[0])
                if can_sort(a[1:], s_new, b):
                    return True
            
            if s:
                b_new = b[:]
                b_new.append(s[-1])
                if can_sort(a, s[:-1], b_new):
                    return True
            
            return False
        
        return can_sort(a, s, b)

    if is_stack_sortable(p):
        print(*p)
    else:
        print("-1")

solve()