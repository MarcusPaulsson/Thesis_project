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
        stack = []
        b = []
        
        def can_sort(a, s, b):
            if not a and not s:
                for i in range(len(b) - 1):
                    if b[i] > b[i+1]:
                        return False
                return True
            
            if a:
                new_s = s + [a[0]]
                new_a = a[1:]
                if can_sort(new_a, new_s, b):
                    return True
            
            if s:
                new_b = b + [s[-1]]
                new_s = s[:-1]
                if can_sort(a, new_s, new_b):
                    return True
            
            return False
        
        return can_sort(arr, [], [])

    if is_stack_sortable(p):
        print(*p)
    else:
        print(-1)

solve()