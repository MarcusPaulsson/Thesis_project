def is_stack_sortable(k, p):
    stack = []
    b = []
    next_to_push = 1
    for i in range(k):
        while next_to_push <= len(p) and (next_to_push in stack or next_to_push in p[:k]):
            next_to_push += 1
        if p[i] < next_to_push:
            return False
        stack.append(p[i])
        while stack and (not b or stack[-1] < b[-1]):
            b.append(stack.pop())
    return True

def restore_permutation(n, k, p):
    if not is_stack_sortable(k, p):
        return -1
    
    remaining_numbers = set(range(1, n + 1)) - set(p)
    result = p.copy()
    
    for _ in range(n - k):
        next_to_add = max(remaining_numbers)
        result.append(next_to_add)
        remaining_numbers.remove(next_to_add)
    
    return result

n, k = map(int, input().split())
p = list(map(int, input().split()))

result = restore_permutation(n, k, p)
if result == -1:
    print(result)
else:
    print(" ".join(map(str, result)))