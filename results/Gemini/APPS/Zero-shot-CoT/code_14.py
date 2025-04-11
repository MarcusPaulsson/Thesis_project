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
        while i < len(arr) or len(s) > 0:
            if len(s) > 0 and (i == len(arr) or s[-1] < arr[i]):
                b.append(s.pop())
            elif i < len(arr):
                s.append(arr[i])
                i += 1
            else:
                return False

        for i in range(len(b) - 1):
            if b[i] > b[i+1]:
                return False
        return True

    if is_stack_sortable(p):
        print(*p)
    else:
        print("-1")

solve()