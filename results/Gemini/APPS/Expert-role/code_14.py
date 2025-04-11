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
            if len(a) > 0 and (len(s) == 0 or a[0] < s[-1]):
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
        
        
        def generate_permutations(index, current_permutation):
            nonlocal result
            if index == n:
                if is_stack_sortable(current_permutation):
                    if result is None or current_permutation > result:
                        result = current_permutation[:]
                return
            
            if index < k:
                generate_permutations(index + 1, current_permutation + [arr[index]])
            else:
                for num in remaining:
                    if num not in current_permutation:
                        new_remaining = remaining[:]
                        new_remaining.remove(num)
                        generate_permutations(index + 1, current_permutation + [num])

        result = None
        
        remaining_nums = []
        for i in range(1, n + 1):
            if i not in arr:
                remaining_nums.append(i)
        
        remaining_nums.sort(reverse=True)
        
        def backtrack(index, current_permutation, remaining_nums):
            nonlocal result
            if index == n:
                if is_stack_sortable(current_permutation):
                    if result is None or current_permutation > result:
                        result = current_permutation[:]
                return
            
            if index < k:
                backtrack(index + 1, current_permutation + [arr[index]], remaining_nums)
            else:
                for i in range(len(remaining_nums)):
                    num = remaining_nums[i]
                    new_remaining = remaining_nums[:i] + remaining_nums[i+1:]
                    backtrack(index + 1, current_permutation + [num], new_remaining)
        
        backtrack(0, [], remaining_nums)
        return result

    result = find_lexicographically_largest(p, k, used)

    if result is None:
        print("-1")
    else:
        print(*result)

solve()