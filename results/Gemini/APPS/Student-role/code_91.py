def solve():
    n = int(input())
    q = list(map(int, input().split()))
    
    p = [0] * n
    used = [False] * (n + 1)
    
    for i in range(n):
        p[i] = q[i]
        used[q[i]] = True
    
    available = []
    for i in range(1, n + 1):
        if not used[i]:
            available.append(i)
    
    available.sort(reverse=True)
    
    j = 0
    for i in range(n - 1):
        if q[i] == q[i+1]:
            if j >= len(available):
                print("-1")
                return
            p[i] = available[j]
            j += 1
        
    
    
    ok = True
    used_check = [False] * (n + 1)
    for val in p:
        if not (1 <= val <= n):
            ok = False
            break
        if used_check[val]:
            ok = False
            break
        used_check[val] = True
    
    if not ok:
        print("-1")
        return
    
    
    q_check = [0] * n
    q_check[0] = p[0]
    for i in range(1, n):
        q_check[i] = max(q_check[i-1], p[i])
        
    if q_check == q:
        print(*p)
    else:
        print("-1")

t = int(input())
for _ in range(t):
    solve()