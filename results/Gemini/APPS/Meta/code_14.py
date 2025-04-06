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
    
    p = p + remaining
    
    def is_stack_sortable(arr):
        s = []
        b = []
        i = 0
        
        while i < len(arr) or len(s) > 0:
            if len(arr) > i and (len(s) == 0 or arr[i] < s[-1]):
                s.append(arr[i])
                i += 1
            elif len(s) > 0:
                b.append(s.pop())
            else:
                return False
        return all(b[i] <= b[i+1] for i in range(len(b)-1))
    
    import itertools
    
    
    remaining_len = n - k
    
    possible_remaining = []

    def find_lexicographically_largest_stack_sortable(current_p, remaining_nums):
        if not remaining_nums:
            if is_stack_sortable(current_p):
                return current_p
            else:
                return None
        
        remaining_nums.sort(reverse=True)
        
        for i in range(len(remaining_nums)):
            next_num = remaining_nums[i]
            next_remaining_nums = remaining_nums[:i] + remaining_nums[i+1:]
            
            result = find_lexicographically_largest_stack_sortable(current_p + [next_num], next_remaining_nums)
            if result:
                return result
        
        return None
    
    remaining_nums = []
    for i in range(1, n + 1):
        if i not in p[:k]:
            remaining_nums.append(i)
    
    
    result = find_lexicographically_largest_stack_sortable(p[:k], remaining_nums)
    
    if result:
        print(*result)
    else:
        print("-1")

solve()