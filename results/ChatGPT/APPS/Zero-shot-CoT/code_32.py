n = int(input())
current_position = 0  # Position in kilometers from the North Pole (0 to 20000)

for _ in range(n):
    t, direction = input().split()
    t = int(t)

    if current_position == 0 and direction != "South":
        print("NO")
        exit()
    if current_position == 20000 and direction != "North":
        print("NO")
        exit()

    if direction == "South":
        current_position += t
    elif direction == "North":
        current_position -= t
    elif direction == "East" or direction == "West":
        # East and West do not change the position in terms of North-South
        continue

    if current_position < 0 or current_position > 20000:
        print("NO")
        exit()

if current_position != 0:
    print("NO")
else:
    print("YES")