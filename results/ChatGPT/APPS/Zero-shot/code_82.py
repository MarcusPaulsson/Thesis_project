n = int(input())
current_distance = 0  # Distance from the North Pole

for _ in range(n):
    t, direction = input().split()
    t = int(t)

    if current_distance == 0 and direction != "South":
        print("NO")
        exit()
    if current_distance == 20000 and direction != "North":
        print("NO")
        exit()

    if direction == "North":
        current_distance -= t
    elif direction == "South":
        current_distance += t
    elif direction in ["West", "East"]:
        # Moving west or east does not change the distance from the poles
        continue

    if current_distance < 0 or current_distance > 20000:
        print("NO")
        exit()

if current_distance != 0:
    print("NO")
else:
    print("YES")