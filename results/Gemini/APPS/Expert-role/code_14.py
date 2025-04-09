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

    p_extended = p[:]
    for x in remaining:
        p_extended.append(x)

    def is_stack_sortable(arr):
        a = arr[:]
        s = []
        b = []
        
        i = 0
        
        while a or s:
            
            can_push = len(a) > 0
            can_pop = len(s) > 0
            
            if can_push and can_pop and a[0] < s[-1]:
                s.append(a.pop(0))
            elif can_pop:
                b.append(s.pop())
            elif can_push:
                s.append(a.pop(0))
            else:
                return False
        
        for i in range(len(b) - 1):
            if b[i] > b[i+1]:
                return False
        return True

    if is_stack_sortable(p_extended):
        print(*p_extended)
    else:
        print("-1")

solve()