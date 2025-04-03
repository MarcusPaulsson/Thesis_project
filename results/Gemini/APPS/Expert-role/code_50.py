def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = float('inf')
    
    for i in range(2 * n + 1):
        for j in range(i + 1):
            left = j
            right = i - j
            
            if left > n or right > n:
                continue
            
            temp_a = a[:]
            
            for k in range(left):
                temp_a[n-1-k] = -1
            
            for k in range(right):
                temp_a[n+k] = -1
                
            strawberries = 0
            blueberries = 0
            
            for k in range(2 * n):
                if temp_a[k] != -1:
                    if temp_a[k] == 1:
                        strawberries += 1
                    else:
                        blueberries += 1
            
            if strawberries == blueberries:
                ans = min(ans, i)
    
    print(ans)

t = int(input())
for _ in range(t):
    solve()