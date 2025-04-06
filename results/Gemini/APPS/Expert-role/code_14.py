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
        i = 0
        j = 0
        while i < len(arr) or len(s) > 0:
            if len(s) > 0 and s[-1] == min(arr[i:] + s):
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
    

    def find_lexicographically_maximal_permutation(n, k, given_p):
        used = set(given_p)
        remaining = []
        for i in range(n, 0, -1):
            if i not in used:
                remaining.append(i)
        
        import itertools
        
        best_p = None
        
        for perm in itertools.permutations(remaining):
            curr_p = given_p + list(perm)
            if is_stack_sortable(curr_p):
                if best_p is None:
                    best_p = curr_p
                else:
                    if curr_p > best_p:
                        best_p = curr_p
        
        return best_p
    
    
    result = find_lexicographically_maximal_permutation(n, k, p[:k])
    
    if result is None:
        print("-1")
    else:
        print(*result)

solve()