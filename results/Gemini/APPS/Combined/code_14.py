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
        expected = 1
        for x in arr:
            stack.append(x)
            while stack and stack[-1] == expected:
                b.append(stack.pop())
                expected += 1
        return not stack

    
    original_p = p[:k]
    
    
    def find_lexicographically_largest_stack_sortable(n, k, initial_p):
        used = set(initial_p)
        remaining = []
        for i in range(n, 0, -1):
            if i not in used:
                remaining.append(i)

        import itertools
        
        best_p = None
        
        for perm in itertools.permutations(remaining):
            
            current_p = initial_p + list(perm)
            
            if is_stack_sortable(current_p):
                if best_p is None:
                    best_p = current_p
                else:
                    if current_p > best_p:
                        best_p = current_p
        
        return best_p

    result = find_lexicographically_largest_stack_sortable(n, k, original_p)

    if result:
        print(*result)
    else:
        print("-1")

solve()