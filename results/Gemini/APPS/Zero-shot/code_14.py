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
        s = []
        b = []
        a = arr[:]
        
        i = 0
        while i < 2 * n:
            if len(a) > 0 and (len(s) == 0 or a[0] < (s[-1] if len(s) > 0 else float('inf'))):
                s.append(a[0])
                a = a[1:]
            elif len(s) > 0:
                b.append(s[-1])
                s = s[:-1]
            else:
                return False
            i += 1
        
        return all(b[i] <= b[i+1] for i in range(len(b)-1))

    
    def find_lexicographically_maximal_permutation(n, k, initial_p):
        used = set(initial_p)
        remaining = []
        for i in range(n, 0, -1):
            if i not in used:
                remaining.append(i)

        import itertools
        
        best_permutation = None
        
        for perm in itertools.permutations(remaining):
            candidate_p = initial_p + list(perm)
            
            if is_stack_sortable(candidate_p):
                if best_permutation is None:
                    best_permutation = candidate_p
                else:
                    if candidate_p > best_permutation:
                        best_permutation = candidate_p
        
        return best_permutation

    result = find_lexicographically_maximal_permutation(n, k, p[:k])
    
    if result is None:
        print("-1")
    else:
        print(*result)

solve()