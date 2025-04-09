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
            if len(a) > 0 and (len(s) == 0 or a[0] < (s[-1])):
                s.append(a[0])
                a.pop(0)
                i += 1
            elif len(s) > 0:
                b.append(s[-1])
                s.pop()
                i += 1
            else:
                break

        if len(s) == 0 and len(a) == 0:
            for i in range(len(b) - 1):
                if b[i] > b[i+1]:
                    return False
            return True
        else:
            return False

    if not is_stack_sortable(p_full):
        print("-1")
        return

    
    def generate_permutations(arr, k):
        
        used_nums = set(arr[:k])
        nums_to_fill = []
        for i in range(1, n + 1):
            if i not in used_nums:
                nums_to_fill.append(i)
        nums_to_fill.sort(reverse=True)

        
        def backtrack(index, current_permutation):
            if index == n:
                return current_permutation[:]
            
            if index < k:
                return backtrack(index + 1, current_permutation)

            
            for num in nums_to_fill:
                if num not in current_permutation:
                    current_permutation.append(num)
                    
                    new_nums_to_fill = nums_to_fill[:]
                    new_nums_to_fill.remove(num)
                    
                    temp_result = backtrack(index + 1, current_permutation)
                    if temp_result:
                        return temp_result
                    
                    current_permutation.pop()
            return None

        result = backtrack(0, arr[:k])
        return result

    
    lexicographically_max_permutation = generate_permutations(p[:], k)

    if lexicographically_max_permutation:
        if is_stack_sortable(lexicographically_max_permutation):
            print(*lexicographically_max_permutation)
        else:
            print("-1")
    else:
        print("-1")


solve()