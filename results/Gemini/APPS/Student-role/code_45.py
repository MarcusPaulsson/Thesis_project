def solve():
    x = int(input())
    
    count = 0
    stair_cells = 1
    total_cells = 0
    
    while total_cells + stair_cells <= x:
        total_cells += stair_cells
        count += 1
        stair_cells = stair_cells * 4 + 1
        
    print(count)

t = int(input())
for _ in range(t):
    solve()