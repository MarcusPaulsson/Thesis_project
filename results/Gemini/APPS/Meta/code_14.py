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
        s = []
        b = []
        a = arr[:]
        
        i = 0
        while i < 2 * n:
            if len(a) > 0 and (len(s) == 0 or a[0] < (s[-1] if len(s) > 0 else float('inf'))):
                s.append(a[0])
                a = a[1:]
                i += 1
            elif len(s) > 0:
                b.append(s[-1])
                s = s[:-1]
                i += 1
            else:
                return False
        
        for i in range(len(b) - 1):
            if b[i] > b[i+1]:
                return False
        return True

    
    def find_lexicographically_largest(arr, k, used):
        remaining = []
        for i in range(n, 0, -1):
            if not used[i]:
                remaining.append(i)

        import itertools
        
        perms = []
        for perm in itertools.permutations(remaining):
            temp_arr = arr[:]
            temp_arr.extend(list(perm))
            perms.append(temp_arr)
        
        
        stack_sortable_perms = []
        for perm in perms:
            if is_stack_sortable(perm):
                stack_sortable_perms.append(perm)
        
        if not stack_sortable_perms:
            return None
        
        
        lexicographically_largest = stack_sortable_perms[0]
        for perm in stack_sortable_perms[1:]:
            if perm > lexicographically_largest:
                lexicographically_largest = perm
        
        return lexicographically_largest
    
    
    result = find_lexicographically_largest(p, k, used)
    
    if result is None:
        print("-1")
    else:
        print(*result)

solve()