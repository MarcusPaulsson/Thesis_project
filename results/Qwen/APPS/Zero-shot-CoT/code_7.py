def barn_empty_day(n, m):
    day = 0
    grains = n
    while grains > 0:
        day += 1
        grains += m
        grains -= day
    return day

n, m = map(int, input().split())
print(barn_empty_day(n, m))