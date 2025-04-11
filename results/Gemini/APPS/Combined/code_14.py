def is_stack_sortable(arr):
    stack = []
    expected = 1
    for num in arr:
        stack.append(num)
        while stack and stack[-1] == expected:
            stack.pop()
            expected += 1
    return not stack

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
    
    
    def find_lexicographically_largest_stack_sortable(prefix, remaining_numbers, n):
        if not remaining_numbers:
            if is_stack_sortable(prefix):
                return prefix
            else:
                return None

        
        for i in range(len(remaining_numbers)):
            
            new_prefix = prefix + [remaining_numbers[i]]
            new_remaining = remaining_numbers[:i] + remaining_numbers[i+1:]
            
            result = find_lexicographically_largest_stack_sortable(new_prefix, new_remaining, n)
            if result:
                return result
        
        return None
    
    remaining_nums = []
    for i in range(1, n + 1):
        if i not in p:
            remaining_nums.append(i)
    
    remaining_nums.sort(reverse=True)
    
    result = find_lexicographically_largest_stack_sortable(p, remaining_nums, n)
    
    if result:
        print(*result)
    else:
        print("-1")

solve()