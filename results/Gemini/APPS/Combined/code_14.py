def is_stack_sortable(arr):
    stack = []
    expected = 1
    for x in arr:
        while stack and stack[-1] == expected:
            stack.pop()
            expected += 1
        if x == expected:
            expected += 1
        elif stack and stack[-1] < x:
            return False
        else:
            stack.append(x)
    while stack:
        if stack[-1] == expected:
            stack.pop()
            expected += 1
        else:
            return False
    return True

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
    
    
    import itertools
    
    best_permutation = None
    
    for permutation in itertools.permutations(remaining):
        candidate = p + list(permutation)
        if is_stack_sortable(candidate):
            if best_permutation is None:
                best_permutation = candidate
            elif candidate > best_permutation:
                best_permutation = candidate
                
    if best_permutation:
        print(*best_permutation)
    else:
        print("-1")
solve()