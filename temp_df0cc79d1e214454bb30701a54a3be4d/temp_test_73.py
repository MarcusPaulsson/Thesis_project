def solve():
    n = int(input())
    a = list(map(int, input().split()))

    def mex(arr):
        seen = set(arr)
        for i in range(n + 1):
            if i not in seen:
                return i
        return n + 1

    ops = []
    
    for _ in range(2 * n):
        
        is_sorted = True
        for i in range(n - 1):
            if a[i] > a[i+1]:
                is_sorted = False
                break
        
        if is_sorted:
            break

        m = mex(a)

        if m < n:
            for i in range(n):
                if a[i] != i and a[i] > m:
                    a[i] = m
                    ops.append(i + 1)
                    break
            else:
                for i in range(n):
                    if a[i] != i:
                        a[i] = m
                        ops.append(i+1)
                        break
        else:
            
            for i in range(n-1):
                if a[i] > a[i+1]:
                    a[i+1] = m
                    ops.append(i+2)
                    break
    
    is_sorted = True
    for i in range(n - 1):
        if a[i] > a[i+1]:
            is_sorted = False
            break
            
    if not is_sorted:
        for i in range(n):
            a[i] = i
            ops.append(i+1)
    
    print(len(ops))
    print(*ops)

t = int(input())
for _ in range(t):
    solve()