def solve():
    x = int(input())
    
    count = 0
    total_cells = 0
    stair_size = 1
    
    while True:
        cells_needed = stair_size * (stair_size + 1) // 2
        if total_cells + cells_needed <= x:
            count += 1
            total_cells += cells_needed
            stair_size = stair_size * 2 + 1
        else:
            break
            
    print(count)

t = int(input())
for _ in range(t):
    solve()