def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    results = []
    
    for l1 in range(1, n):
        l2 = n - l1
        p1 = a[:l1]
        p2 = a[l1:]
        
        m1 = max(p1)
        m2 = max(p2)
        
        if all(1 <= x <= m1 for x in p1) and all(1 <= x <= m2 for x in p2) and len(set(p1)) == l1 and len(set(p2)) == l2 and m1 == l1 and m2 == l2:
            results.append((l1, l2))
            
    print(len(results))
    for l1, l2 in results:
        print(l1, l2)

t = int(input())
for _ in range(t):
    solve()