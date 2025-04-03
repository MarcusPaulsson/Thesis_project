def create_grid(n, k):
    grid = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if k > 0:
                grid[i][(i + j) % n] = 1
                k -= 1
    return grid

def min_f(n, k):
    if k == 0:
        return 0, [['0'] * n for _ in range(n)]
    if k == n * n:
        return 0, [['1'] * n for _ in range(n)]
    
    r = k // n
    c = k % n
    
    grid = [['0'] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(r):
            grid[i][(i + j) % n] = '1'
    
    for j in range(c):
        grid[j][(n - 1 - j) % n] = '1'
    
    return ((r + 1) ** 2 - r ** 2) + ((1 ** 2 - 0 ** 2) if c > 0 else 0), grid

t = int(input())
results = []
for _ in range(t):
    n, k = map(int, input().split())
    f_value, grid = min_f(n, k)
    results.append(f_value)
    results.extend(''.join(row) for row in grid)

print('\n'.join(map(str, results)))