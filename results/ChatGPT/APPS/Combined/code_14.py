def restore_stack_sortable_permutation(n, k, p):
    used = set(p)
    result = p[:]
    stack = []
    next_num = n

    for i in range(k):
        while stack and stack[-1] < next_num:
            result.append(stack.pop())

        if p[i] != next_num:
            while next_num > 0 and next_num not in used:
                stack.append(next_num)
                next_num -= 1

        if p[i] != next_num:
            return -1

        next_num -= 1

    while stack:
        result.append(stack.pop())

    return result

# Input reading
n, k = map(int, input().split())
p = list(map(int, input().split()))

# Get the result and print
result = restore_stack_sortable_permutation(n, k, p)
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))