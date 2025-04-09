def solve():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    available = set(range(1, n + 1))
    for x in p:
        available.remove(x)

    def is_stack_sortable(arr):
        stack = []
        b = []
        i = 0
        while i < len(arr) or stack:
            if i < len(arr):
                stack.append(arr[i])
                i += 1
            else:
                
                b.append(stack.pop())
                continue

            while stack and stack[-1] == min(stack):
                b.append(stack.pop())
        
        return all(b[i] <= b[i+1] for i in range(len(b)-1))

    def find_permutation(current_permutation, remaining_available):
        if len(current_permutation) == n:
            if is_stack_sortable(current_permutation):
                return current_permutation
            else:
                return None

        for val in sorted(list(remaining_available), reverse=True):
            new_permutation = current_permutation + [val]
            new_available = remaining_available - {val}
            result = find_permutation(new_permutation, new_available)
            if result:
                return result

        return None

    remaining_available = available
    result = find_permutation(p, remaining_available)

    if result:
        print(*result)
    else:
        print(-1)

solve()