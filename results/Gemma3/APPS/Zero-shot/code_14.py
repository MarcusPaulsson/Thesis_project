def solve():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    
    remaining = []
    for i in range(1, n + 1):
        if i not in p:
            remaining.append(i)
    
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
        
        return result == sorted(arr)
    
    import itertools
    
    best_permutation = -1
    
    for perm in itertools.permutations(remaining):
        current_permutation = p + list(perm)
        
        if is_stack_sortable(current_permutation):
            if best_permutation == -1 or current_permutation > best_permutation:
                best_permutation = current_permutation
    
    if best_permutation != -1:
        print(*best_permutation)
    else:
        print(-1)

solve()