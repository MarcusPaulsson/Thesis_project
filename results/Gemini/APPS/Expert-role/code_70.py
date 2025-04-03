def solve():
    n, k = map(int, input().split())
    s = input()
    
    ans = 0
    for i in range(k // 2):
        counts = {}
        for j in range(0, n, k):
            c1 = s[i+j]
            c2 = s[k - 1 - i + j]
            counts[c1] = counts.get(c1, 0) + 1
            counts[c2] = counts.get(c2, 0) + 1
        
        max_count = 0
        total = 0
        for c in counts:
            max_count = max(max_count, counts[c])
            total += counts[c]
        
        ans += (total - max_count)
    
    if k % 2 == 1:
        counts = {}
        for j in range(0, n, k):
            c = s[k // 2 + j]
            counts[c] = counts.get(c, 0) + 1
        
        max_count = 0
        total = 0
        for c in counts:
            max_count = max(max_count, counts[c])
            total += counts[c]
        
        ans += (total - max_count)
    
    print(ans)

t = int(input())
for _ in range(t):
    solve()