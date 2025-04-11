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
    p_full.extend(remaining)

    def is_stack_sortable(arr):
        stack = []
        output = []
        
        for num in arr:
            stack.append(num)
            while stack and stack[-1] == len(output) + 1:
                output.append(stack.pop())
        
        return len(output) == len(arr)

    if is_stack_sortable(p_full):
        print(*p_full)
    else:
        print("-1")

solve()