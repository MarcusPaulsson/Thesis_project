def max_nice_staircases(x):
    n = 0
    total_cells = 0
    while total_cells <= x:
        n += 1
        total_cells += n * (n + 1) // 2  # sum of first n natural numbers
    return n - 1

t = int(input())
for _ in range(t):
    x = int(input())
    print(max_nice_staircases(x))