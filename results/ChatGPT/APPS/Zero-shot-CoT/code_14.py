def is_stack_sortable(p):
    s = []
    b = []
    for num in p:
        while s and (not b or s[-1] < b[-1]):
            b.append(s.pop())
        s.append(num)
    while s:
        b.append(s.pop())
    return b == sorted(b)

def restore_permutation(n, k, given):
    used = set(given)
    remaining = [x for x in range(1, n + 1) if x not in used]
    
    if not is_stack_sortable(given + remaining):
        return -1

    # Construct the lexicographically maximal permutation
    result = given.copy()
    remaining.sort(reverse=True)
    
    # Add the remaining elements to result
    result += remaining
    return result

# Input reading
n, k = map(int, input().split())
given = list(map(int, input().split()))

# Get the result
result = restore_permutation(n, k, given)

# Output the result
if result == -1:
    print(result)
else:
    print(' '.join(map(str, result)))