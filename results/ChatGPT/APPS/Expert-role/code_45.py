def count_nice_staircases(x):
    count = 0
    n = 1
    total_cells = 0
    
    while True:
        total_cells += n * (n + 1) // 2  # Sum of first n natural numbers (1 + 2 + ... + n)
        if total_cells > x:
            break
        count += 1
        n += 1
    
    return count

t = int(input())
for _ in range(t):
    x = int(input())
    print(count_nice_staircases(x))