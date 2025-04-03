def solve():
    n, k = map(int, input().split())
    s = input()
    
    ans = 0
    for i in range(k // 2):
        counts = {}
        for j in range(0, n, k):
            char1 = s[i + j]
            char2 = s[k - 1 - i + j]
            
            if char1 not in counts:
                counts[char1] = 0
            counts[char1] += 1
            
            if char2 not in counts:
                counts[char2] = 0
            counts[char2] += 1
        
        total_chars = sum(counts.values())
        max_count = 0
        for count in counts.values():
            max_count = max(max_count, count)
        
        ans += total_chars - max_count
    
    if k % 2 == 1:
        counts = {}
        for j in range(0, n, k):
            char = s[k // 2 + j]
            if char not in counts:
                counts[char] = 0
            counts[char] += 1
        
        total_chars = sum(counts.values())
        max_count = 0
        for count in counts.values():
            max_count = max(max_count, count)
        
        ans += total_chars - max_count
    
    print(ans)

t = int(input())
for _ in range(t):
    solve()