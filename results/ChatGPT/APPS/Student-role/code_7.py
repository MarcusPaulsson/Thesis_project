n, m = map(int, input().split())

day = 0
grains = n

while grains > 0:
    day += 1
    grains += m
    if grains > n:
        grains = n
    grains -= day

print(day)