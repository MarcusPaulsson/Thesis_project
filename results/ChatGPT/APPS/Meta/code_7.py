n, m = map(int, input().split())

day = 0
grains = n

while grains > 0:
    day += 1
    grains += m  # Grains are brought to the barn
    if grains > n:
        grains = n  # Barn can't exceed its capacity

    grains -= day  # Sparrows eat grains
    if grains <= 0:  # Check if the barn is empty
        break

print(day)