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
    for x in remaining:
        p_full.append(x)

    def is_stack_sortable(arr):
        stack = []
        expected = 1
        for x in arr:
            stack.append(x)
            while stack and stack[-1] == expected:
                stack.pop()
                expected += 1
        return not stack

    if not is_stack_sortable(p_full):
        print("-1")
        return

    print(*p_full)

solve()