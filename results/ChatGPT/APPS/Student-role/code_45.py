def max_nice_staircases(x):
    count = 0
    n = 1
    while x >= n * (n + 1) // 2:
        count += 1
        x -= n * (n + 1) // 2
        n += 1
    return count

t = int(input())
for _ in range(t):
    x = int(input())
    print(max_nice_staircases(x))