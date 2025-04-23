def restore_stack_sortable_permutation(n, k, given):
    used = set(given)
    result = list(given)
    stack = []
    next_number = n

    for i in range(k - 1, -1, -1):
        while next_number > 0 and next_number not in used:
            stack.append(next_number)
            next_number -= 1

        if stack and stack[-1] > result[i]:
            return -1

        while stack and stack[-1] <= result[i]:
            result.append(stack.pop())

        result.append(result[i])

    while stack:
        result.append(stack.pop())

    if len(result) != n:
        return -1

    return result

# Input reading
n, k = map(int, input().split())
given = list(map(int, input().split()))

# Get the result
result = restore_stack_sortable_permutation(n, k, given)

# Print the result
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))