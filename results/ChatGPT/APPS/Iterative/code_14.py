def is_stack_sortable(p):
    stack = []
    b = []
    index = 0
    n = len(p)

    for x in range(1, n + 1):
        while stack and stack[-1] == p[index]:
            b.append(stack.pop())
            index += 1
        if index < n and p[index] == x:
            b.append(x)
            index += 1
        else:
            stack.append(x)

    while stack:
        b.append(stack.pop())

    return b == sorted(b)

def restore_permutation(n, k, p):
    used = set(p)
    remaining = [x for x in range(1, n + 1) if x not in used]
    
    if not is_stack_sortable(p + remaining):
        return -1

    result = p.copy()
    remaining.sort(reverse=True)
    j = 0

    for x in remaining:
        while j < len(remaining) and (not result or x > remaining[j]):
            result.append(remaining[j])
            j += 1
            
    return result

n, k = map(int, input().split())
p = list(map(int, input().split()))

result = restore_permutation(n, k, p)
if result == -1:
    print(-1)
else:
    print(" ".join(map(str, result)))