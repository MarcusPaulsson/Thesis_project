def solve():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    available = [True] * (n + 1)
    for x in p:
        available[x] = False

    remaining = []
    for i in range(n, 0, -1):
        if available[i]:
            remaining.append(i)

    p_full = p[:]
    for i in range(n - k):
        p_full.append(remaining[i])

    def is_stack_sortable(arr):
        stack = []
        b = []
        idx = 0
        for i in range(2 * len(arr)):
            if idx < len(arr) and (not stack or arr[idx] < stack[-1]):
                stack.append(arr[idx])
                idx += 1
            elif stack:
                b.append(stack.pop())
            else:
                return False

        for i in range(len(b) - 1):
            if b[i] > b[i+1]:
                return False
        return True

    if is_stack_sortable(p_full):
        print(*p_full)
    else:
        print("-1")

solve()