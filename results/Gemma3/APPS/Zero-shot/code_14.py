def solve():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    
    remaining = []
    for i in range(1, n + 1):
        if i not in p:
            remaining.append(i)
    
    remaining.sort(reverse=True)
    
    def is_stack_sortable(arr):
        stack = []
        result = []
        
        for x in arr:
            stack.append(x)
            while stack and result and stack[-1] < result[-1]:
                return False
            
            while stack and (not result or stack[-1] <= result[-1]):
                result.append(stack.pop())
        
        while stack:
            if result and stack[-1] < result[-1]:
                return False
            result.append(stack.pop())
        
        return all(result[i] <= result[i+1] for i in range(len(result)-1))
    
    
    import itertools
    
    for perm in itertools.permutations(remaining):
        temp_p = p + list(perm)
        if is_stack_sortable(temp_p):
            print(*temp_p)
            return
    
    print(-1)

solve()