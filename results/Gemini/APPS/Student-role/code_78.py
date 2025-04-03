def solve():
    n, m = map(int, input().split())
    grid = [input() for _ in range(n)]
    
    ans = float('inf')
    
    for r in range(1, n + 1):
        for c in range(1, m + 1):
            
            cost = 0
            
            # Check row r
            for j in range(m):
                if grid[r-1][j] == '.':
                    cost += 1
            
            # Check col c
            for i in range(n):
                if grid[i][c-1] == '.':
                    cost += 1
            
            # Avoid double counting
            if grid[r-1][c-1] == '*':
                cost -= 1
                
            ans = min(ans, cost)
            
    print(ans)

q = int(input())
for _ in range(q):
    solve()