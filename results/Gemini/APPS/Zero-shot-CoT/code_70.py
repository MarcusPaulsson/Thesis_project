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
            if char2 not in counts:
                counts[char2] = 0
                
            counts[char1] += 1
            counts[char2] += 1
            
        total = 0
        max_count = 0
        for char in counts:
            total += counts[char]
            max_count = max(max_count, counts[char])
        
        ans += (total - max_count)

    if k % 2 == 1:
        counts = {}
        mid = k // 2
        for j in range(0, n, k):
            char = s[mid + j]
            if char not in counts:
                counts[char] = 0
            counts[char] += 1
            
        total = 0
        max_count = 0
        for char in counts:
            total += counts[char]
            max_count = max(max_count, counts[char])
            
        ans += (total - max_count)

    print(ans)

t = int(input())
for _ in range(t):
    solve()