def solve():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    used = [False] * (n + 1)
    for x in p:
        used[x] = True

    remaining = []
    for i in range(n, 0, -1):
        if not used[i]:
            remaining.append(i)

    p_full = p[:]
    for x in remaining:
        p_full.append(x)

    def is_stack_sortable(arr):
        stack = []
        b = []
        a = arr[:]
        
        def backtrack():
            nonlocal a, stack, b
            
            if not a and not stack:
                return all(b[i] <= b[i+1] for i in range(len(b)-1)) if len(b) > 1 else True
            
            
            if a:
                stack.append(a[0])
                new_a = a[1:]
                
                old_a = a[:]
                old_stack = stack[:-1]
                old_b = b[:]
                
                a = new_a
                
                if backtrack():
                    return True
                
                a = old_a
                stack = old_stack
                b = old_b
            
            if stack:
                b.append(stack[-1])
                new_stack = stack[:-1]
                
                old_a = a[:]
                old_stack = stack[:]
                old_b = b[:-1]
                
                stack = new_stack
                
                if backtrack():
                    return True
                
                a = old_a
                stack = old_stack
                b = old_b
            
            return False

        return backtrack()

    if not is_stack_sortable(p_full):
        print(-1)
        return

    remaining = []
    for i in range(n, 0, -1):
        if not used[i]:
            remaining.append(i)

    best_p = None
    import itertools
    for perm in itertools.permutations(remaining):
        candidate_p = p + list(perm)
        if is_stack_sortable(candidate_p):
            if best_p is None:
                best_p = candidate_p
            else:
                if candidate_p > best_p:
                    best_p = candidate_p

    if best_p is None:
        print(-1)
    else:
        print(*best_p)

solve()