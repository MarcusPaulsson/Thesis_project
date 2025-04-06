def is_stack_sortable(arr):
    stack = []
    b = []
    expected = 1

    for x in arr:
        stack.append(x)
        while stack and stack[-1] == expected:
            b.append(stack.pop())
            expected += 1

    while stack:
        b.append(stack.pop())
    
    return b == sorted(arr)


def solve():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    
    used = set(p)
    remaining = []
    for i in range(n, 0, -1):
        if i not in used:
            remaining.append(i)
    
    def find_permutation(index, current_permutation):
        if index == n:
            if is_stack_sortable(current_permutation):
                return current_permutation
            else:
                return None
        
        if index < k:
            return find_permutation(index + 1, current_permutation)
        else:
            for i in range(len(remaining) - 1, -1, -1):
                num = remaining[i]
                new_remaining = remaining[:i] + remaining[i+1:]
                
                result = find_permutation(index + 1, current_permutation + [num])
                if result:
                    return result
            return None
    
    result = find_permutation(k, p)
    
    if result:
        print(*result)
    else:
        print(-1)

solve()