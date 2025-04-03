def solve():
    n, k = map(int, input().split())
    
    grid = [['0'] * n for _ in range(n)]
    
    row = 0
    col = 0
    
    for _ in range(k):
        grid[row][col] = '1'
        row = (row + 1) % n
        col = (col + 1) % n
        if row == 0:
            col = (col + 1) % n

    rows_sums = [0] * n
    cols_sums = [0] * n
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '1':
                rows_sums[i] += 1
                cols_sums[j] += 1
    
    f_a = (max(rows_sums) - min(rows_sums))**2 + (max(cols_sums) - min(cols_sums))**2
    
    print(f_a)
    for row in grid:
        print("".join(row))

t = int(input())
for _ in range(t):
    solve()