def solve():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    used = set(p)
    remaining = []
    for i in range(n, 0, -1):
        if i not in used:
            remaining.append(i)

    p += remaining

    def is_stack_sortable(arr):
        s = []
        b = []
        i = 0
        j = 0
        while i < len(arr) or len(s) > 0:
            if len(s) > 0 and s[-1] == min(arr[i:] + s):
                b.append(s[-1])
                s.pop()
            elif i < len(arr):
                s.append(arr[i])
                i += 1
            else:
                return False
        
        return all(b[i] <= b[i+1] for i in range(len(b)-1))

    if is_stack_sortable(p):
        print(*p)
    else:
        print("-1")

solve()