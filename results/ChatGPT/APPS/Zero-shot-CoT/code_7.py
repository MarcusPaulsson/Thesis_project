def day_when_barn_empty(n, m):
    day = 0
    total_eaten = 0
    current_grains = n

    while current_grains > 0:
        day += 1
        total_eaten += day
        current_grains += m
        if current_grains > n:
            current_grains = n
        current_grains -= total_eaten

    return day

# Read input
n, m = map(int, input().split())
print(day_when_barn_empty(n, m))