def solve():
    n, k = map(int, input().split())
    s = input()
    
    ans = 0
    for i in range(k // 2):
        counts = {}
        for j in range(0, n, k):
            counts[s[i+j]] = counts.get(s[i+j], 0) + 1
            counts[s[k-1-i+j]] = counts.get(s[k-1-i+j], 0) + 1
        
        max_count = 0
        total_count = 0
        for count in counts.values():
            max_count = max(max_count, count)
            total_count += count
            
        ans += (total_count - max_count)
        
    if k % 2 == 1:
        counts = {}
        for j in range(0, n, k):
            counts[s[k//2+j]] = counts.get(s[k//2+j], 0) + 1
            
        max_count = 0
        total_count = 0
        for count in counts.values():
            max_count = max(max_count, count)
            total_count += count
        ans += (total_count - max_count)
    
    print(ans)

t = int(input())
for _ in range(t):
    solve()