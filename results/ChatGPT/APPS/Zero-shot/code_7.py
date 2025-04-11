def find_empty_day(n, m):
    day = 0
    total_sparrows = 0
    while n > 0:
        day += 1
        total_sparrows += day
        n = min(n + m, n) - total_sparrows
    return day

n, m = map(int, input().split())
print(find_empty_day(n, m))