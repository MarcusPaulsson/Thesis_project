def is_stack_sortable(n, k, p):
    stack = []
    remaining = set(range(1, n + 1)) - set(p)
    answer = p[:]

    # Check if the first k elements are already in descending order
    for i in range(1, k):
        if p[i] > p[i - 1]:
            return -1

    # Fill the remaining part of the permutation
    for i in range(k, n):
        # Take the maximum element that can be added
        if remaining:
            max_remain = max(remaining)
        else:
            max_remain = 0
        
        if not stack or (stack and stack[-1] > max_remain):
            answer.append(p[i - k])  # Append the last p element if we can
        else:
            answer.append(max_remain)
            remaining.remove(max_remain)

        # Push to stack if possible
        while remaining and (not stack or stack[-1] < max(remaining)):
            stack.append(max(remaining))
            remaining.remove(max(remaining))

    # Finalize the answer
    while stack:
        answer.append(stack.pop())

    # Validate the final permutation
    if sorted(answer) == list(range(1, n + 1)):
        return answer
    else:
        return -1

# Input reading
n, k = map(int, input().split())
p = list(map(int, input().split()))

result = is_stack_sortable(n, k, p)
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))