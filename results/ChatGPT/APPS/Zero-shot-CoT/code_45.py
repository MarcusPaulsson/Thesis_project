def max_nice_staircases(x):
    count = 0
    stairs = 1
    total_cells = 0
    
    while total_cells + stairs <= x:
        total_cells += stairs
        count += 1
        stairs += 1
    
    return count

t = int(input())
for _ in range(t):
    x = int(input())
    print(max_nice_staircases(x))