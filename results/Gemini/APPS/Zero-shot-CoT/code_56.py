def solve():
    n, k = map(int, input().split())
    
    grid = [[0] * n for _ in range(n)]
    
    row = 0
    col = 0
    
    for _ in range(k):
        grid[row][col] = 1
        row = (row + 1) % n
        col = (col + 1) % n
        if grid[row][col] == 1:
            col = (col + 1) % n

    
    rows_sums = [sum(row) for row in grid]
    cols_sums = [sum(grid[i][j] for i in range(n)) for j in range(n)]
    
    f_a = (max(rows_sums) - min(rows_sums))**2 + (max(cols_sums) - min(cols_sums))**2
    
    print(f_a)
    for row in grid:
        print("".join(map(str, row)))
    


t = int(input())
for _ in range(t):
    solve()