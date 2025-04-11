n = int(input())
position = 0  # Position on the meridian, starting at North Pole (0 km)

for _ in range(n):
    t, direction = input().split()
    t = int(t)

    if position == 0 and direction != "South":
        print("NO")
        exit()
    elif position == 20000 and direction != "North":
        print("NO")
        exit()

    if direction == "South":
        position += t
    elif direction == "North":
        position -= t
    elif direction == "West" or direction == "East":
        # Moving West or East does not change the position on the meridian
        continue

    if position < 0 or position > 20000:
        print("NO")
        exit()

if position != 0:
    print("NO")
else:
    print("YES")