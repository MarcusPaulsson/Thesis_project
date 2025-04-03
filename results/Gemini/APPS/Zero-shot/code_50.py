def solve():
    n = int(input())
    a = list(map(int, input().split()))

    ans = float('inf')

    for l in range(n + 1):
        for r in range(n + 1):
            temp_a = a[:]
            
            eaten = []
            
            
            left_idx = n - 1
            right_idx = n
            
            
            for _ in range(l):
                eaten.append(temp_a[left_idx])
                left_idx -= 1
                
            for _ in range(r):
                eaten.append(temp_a[right_idx])
                right_idx += 1
                
            
            remaining_a = []
            for i in range(2 * n):
                if i not in range(left_idx + 1, n) and i not in range(n, right_idx):
                    remaining_a.append(temp_a[i])
                    
            
            strawberry_count = remaining_a.count(1)
            blueberry_count = remaining_a.count(2)
            
            if strawberry_count == blueberry_count:
                ans = min(ans, l + r)
                
    print(ans)


t = int(input())
for _ in range(t):
    solve()