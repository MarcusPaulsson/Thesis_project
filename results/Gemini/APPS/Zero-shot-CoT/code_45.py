def solve():
    x = int(input())
    
    staircases = []
    n = 1
    while True:
        cells_needed = n * (n + 1) // 2
        if cells_needed > x:
            break
        staircases.append(cells_needed)
        n += 1
    
    nice_staircases = []
    n = 1
    while True:
        cells_needed = n * (n + 1) // 2
        if cells_needed > x:
            break
        if is_nice(n):
            nice_staircases.append(cells_needed)
        n += 1
        
    count = 0
    remaining_cells = x
    
    
    n = 1
    cells_used = 0
    while True:
        cells_needed = n * (n + 1) // 2
        if cells_needed > x:
            break
        if is_nice(n):
            if remaining_cells >= cells_needed:
                remaining_cells -= cells_needed
                count += 1
        n+=1
    
    print(count)
    

def is_nice(n):
    if n == 1:
        return True
    if n == 3:
        return True
    
    k = 1
    while True:
        val = (2**k) - 1
        if val > n:
            break
        if val == n:
            return True
        k += 1
    
    return False

t = int(input())
for _ in range(t):
    solve()