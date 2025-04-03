def solve():
    n, m = map(int, input().split())
    grid = [input() for _ in range(n)]
    
    ans = float('inf')
    
    for r in range(n):
        for c in range(m):
            cost = 0
            
            # Cost to make row r black
            for j in range(m):
                if grid[r][j] == '.':
                    cost += 1
            
            # Cost to make col c black
            for i in range(n):
                if grid[i][c] == '.':
                    cost += 1
            
            # Subtract 1 if we double-counted the cell (r, c)
            if grid[r][c] == '*':
                cost -= 1
            
            ans = min(ans, cost)
            
    print(ans)

q = int(input())
for _ in range(q):
    solve()