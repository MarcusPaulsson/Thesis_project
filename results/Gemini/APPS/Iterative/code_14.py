def solve():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    
    used = set(p)
    remaining = sorted(list(set(range(1, n + 1)) - used), reverse=True)
    
    p_full = p + remaining
    
    def is_stack_sortable(arr):
        stack = []
        b = []
        
        for x in arr:
            stack.append(x)
            while stack and stack[-1] == len(b) + 1:
                b.append(stack.pop())
        
        return len(b) == len(arr)
    
    if is_stack_sortable(p_full):
        print(*p_full)
    else:
        print("-1")

solve()